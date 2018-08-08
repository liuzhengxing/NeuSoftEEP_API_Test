# _*_ coding:utf-8 _*_

import unittest
import json

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import exec_oracle
from 测试用例.接口自动化.接口自动化_V2.接口测试.测试套件.生产工单下发 import workorder_changestatus
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物料需求 import MaterialRequirement
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物流单 import Logistics
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物流单报工 import LogBillReport
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.报工记录 import LogReportRecord
from public import params


class TestLogReportRecord(unittest.TestCase):
    """物流报工记录测试类"""

    def setUp(self):
        self.mr = MaterialRequirement()
        self.lg = Logistics()
        self.lbr = LogBillReport()
        self.lrr = LogReportRecord()

        self.materialReq_mock_data = {
            "gids": [],
            "groupBy": [],
            "orderBy": [],
            "strategys": [],
            "strategyGids": []
        }

        self.materialReq_query_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "factoryStationRef.stationName",
                        "type": "eq",
                        "value": "CPU",
                        "left": "(",
                        "right": ")"
                    }
                ],
                "sorted": "createTime desc"
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

        self.lgis_ref_data = {
            "gids": [],
            "groupBy": [],
            "orderBy": []
        }

        self.lgis_query_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": params.busiUnitGid,
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "imeLogTrackBillDetailList.resourceGidRef.code",
                        "type": "eq",
                        "value": "MR201807230023",
                        "left": "(",
                        "right": ")"
                    }
                ]
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

        self.lgis_bind_data = {
            'gids': [],
            'bmLogRouteGid': params.bmLogRouteGid
        }

        self.lbr_mock_data = {
            "billGidList": [],
            "operationRuleList": [
                {
                    "bmLogOperationGid": params.bmLogOperationGid,
                    "ruleList": []
                }
            ]
        }

        self.lbr_find_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": params.busiUnitGid,
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "logBillReportList.resourceGidRef.code",
                        "type": "eq",
                        "value": "TB",
                        "left": "(",
                        "right": ")"
                    }
                ]
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

        self.lrr_query_data = {
            "query": {
                "query": [
                    {
                        "field": "opType",
                        "value": "REPORT",
                        "operator": "and",
                        "type": "eq",
                        "left": "(",
                        "right": ")"
                    },
                    {
                        "operator": "and",
                        "field": "objectGid",
                        "type": "eq",
                        "value": "",
                        "left": "(",
                        "right": ")"
                    }
                ]
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

    def test_logbillreport_1(self):
        """
        整单报工
        :return:
        """
        # 创建工单并下发
        workOrderGidList = workorder_changestatus()

        # 拼接传参
        self.materialReq_mock_data['gids'] = workOrderGidList


        # 参照生成物料需求
        self.mr.materialmrequirement_referenceGeneration = Mock(side_effect=self.mr.materialmrequirement_referenceGeneration)
        resp = self.mr.materialmrequirement_referenceGeneration(self.materialReq_mock_data)
        print('Response：', resp)

        # 执行SQL，为数据添加业务组
        # sql = "UPDATE IME_LOGISTICS_MAT_REQ SET SM_BUSI_GROUP_GID='632cd1f557f0437cbe48a66a0021bd93', " \
        #       "SM_BUSI_UNIT_GID='7e2c4ba1d1f64ad7b214a233c7ebb0fb' " \
        #       "WHERE GID IN (SELECT GID FROM IME_V11.IME_LOGISTICS_MAT_REQ WHERE CREATE_BY LIKE 'Q%')"
        # exec_oracle(sql)

        # 查询物料需求
        # UPDATE IME_LOGISTICS_MAT_REQ SET SM_BUSI_GROUP_GID='632cd1f557f0437cbe48a66a0021bd93',
        # SM_BUSI_UNIT_GID='7e2c4ba1d1f64ad7b214a233c7ebb0fb' WHERE GID IN
        # (SELECT GID FROM IME_V11.IME_LOGISTICS_MAT_REQ WHERE CREATE_BY LIKE 'Q%')
        self.mr.materialmrequirement_queryByData = Mock(side_effect=self.mr.materialmrequirement_queryByData)
        resp_data = self.mr.materialmrequirement_queryByData(self.materialReq_query_data)
        mr_gid = resp_data.get('data')[0].get('gid')
        mr_code = resp_data.get('data')[0].get('code')

        # 参照生成物流单
        mrgidList = []
        mrgidList.append(mr_gid)
        self.lgis_ref_data['gids'] = mrgidList
        self.lg.logistics_referenceGeneration = Mock(side_effect=self.lg.logistics_referenceGeneration)
        resp = self.lg.logistics_referenceGeneration(self.lgis_ref_data)

        # 查询物流单
        self.lgis_query_data['query']['query'][1]['value'] = mr_code
        self.lg.logistics_queryByData = Mock(side_effect=self.lg.logistics_queryByData)
        resp_lg = self.lg.logistics_queryByData(self.lgis_query_data)
        lg_gid = resp_lg.get('data')[0].get('gid')
        lg_code = resp_lg.get('data')[0].get('code')

        # 设置物流单工艺模板
        lgList = []
        lgList.append(lg_gid)
        self.lgis_bind_data['gids'] = lgList
        self.lg.logistics_bindLogRoute = Mock(side_effect=self.lg.logistics_bindLogRoute)
        resp_lg_bind = self.lg.logistics_bindLogRoute(self.lgis_bind_data)

        # 创建物流报工单
        self.lbr_mock_data['billGidList'] = lgList
        self.lbr.logbillreport_createByTrackBill = Mock(side_effect=self.lbr.logbillreport_createByTrackBill)
        resp_lbr_create = self.lbr.logbillreport_createByTrackBill(self.lbr_mock_data)
        lbr_gid_list = resp_lbr_create.get('data')

        # 查询物流报工单
        # self.lbr_find_data['query']['query'][1]['value'] = lg_code
        # self.lbr.logbillreport_queryByData = Mock(side_effect=self.lbr.logbillreport_queryByData)
        # resp_lbr_find = self.lbr.logbillreport_queryByData(self.lbr_find_data)

        # lbr_gid = resp_lbr_find.get('data')[0].get('gid')

        # lbr_gid_list = []
        # resp_gid = resp_lbr_find.get('data')[0].get('gid')
        # lbr_gid_list.append(resp_gid)

        # 整单报工
        self.lbr.logbillreport_reportByBill = Mock(side_effect=self.lbr.logbillreport_reportByBill)
        resp_lbr_report = self.lbr.logbillreport_reportByBill(lbr_gid_list)

        # 查询物流报工记录
        self.lrr_query_data['query']['query'][1]['value'] = lbr_gid_list[0]
        self.lrr.logreportrecord_query = Mock(side_effect=self.lrr.logreportrecord_query)
        resp_lrr_query = self.lrr.logreportrecord_query(self.lrr_query_data)

        self.assertEqual(1, len(resp_lrr_query.get('data')))


if __name__ == '__main__':
    unittest.main()
