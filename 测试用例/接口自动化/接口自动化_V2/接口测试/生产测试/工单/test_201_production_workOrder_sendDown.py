# _*_ coding:utf-8 _*_

import unittest

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.工单 import WorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.生产工艺 import ProdRouteLine
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.派工单 import TrackOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.报工 import ReportOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from public import params


class TestWorkOrderSendDown(unittest.TestCase):
    """工单下发测试类"""

    def setUp(self):
        self.wo = WorkOrder()
        self.prl = ProdRouteLine()
        self.to = TrackOrder()
        self.ro = ReportOrder()
        self.workOrder_mock_data = {
            "code": "",
            "resourceOrderGid": "",
            "materialGid": params.MaterielSJGid,
            "orderType": "62DC90DAFA845CB2E055000000000001",
            "workCenterGid": params.bmFactoryWorkCenterGid,
            "factoryLineGid": params.bmFactoryLineCF,
            "routeLineGid": "",
            "planQty": 10,
            "planBeginTime": "2018-05-01",
            "planEndTime": "2018-05-31",
            "actualBeginTime": "",
            "actualEndTime": "",
            "finishQty": "",
            "measureBeginTime": "",
            "measureEndTime": "",
            "orderSeq": "",
            "parentWorkOrderGid": "",
            "freezeStatus": "",
            "orderStatus": "",
            "bomStatus": "",
            "createStatus": "",
            "roundNum": "",
            "processStatus": "",
            "createKmFlag": "",
            "createQacFlag": "",
            "repairCardGid": "",
            "measurementUnitGid": params.bmMeasurementUnitGid,
            "materialVersion": "1",
            "busiActivityType": "",
            "qualifiedQty": "",
            "unqualifiedQty": "",
            "wasteQty": "",
            "batchNumber": "",
            "productGid": "",
            "workOrderCategory": "",
            "bomVersion": "",
            "routeLineVersion": "",
            "canOperation": "",
            "surplusOrderFlag": "",
            "publishedQty": "",
            "factoryLineType": "",
            "generatedCode": ""
        }
        self.track_query_data = {
            "query": {
                "query": [
                    # {
                    #     # "field": "smBusiGroupGid",
                    #     "field": "smBusiUnitGid",
                    #     "type": "eq",
                    #     # "value": params.busiGroupGid,
                    #     "value": params.busiUnitGid,
                    #     "operator": "and"
                    # },
                    {
                        "operator": "and",
                        "field": "resourceOrderGid",
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

    def test_workorder_senddown_1(self):
        """工单下发接口测试：下发生成派工单"""

        # 工单创建
        code = 'WO' + create_code()
        self.workOrder_mock_data['code'] = code
        self.wo.workorder_create = Mock(side_effect=self.wo.workorder_create)
        resp = self.wo.workorder_create(self.workOrder_mock_data)
        print('Response：', resp)
        # self.assertEqual(self.po.planorder_create(mock_data), mock_resp)

        workOrderGidList = []
        workOrderGid = resp.pop('data')
        workOrderGidList.append(workOrderGid)

        # 工单下发
        self.wo.workorder_release = Mock(side_effect=self.wo.workorder_release)
        self.wo.workorder_release(workOrderGidList)

        # 派工单查询
        self.track_query_data.get('query').get('query')[0]['value'] = workOrderGid
        self.to.trackorder_findByWorkOrderGid = Mock(side_effect=self.to.trackorder_findByWorkOrderGid)
        resp = self.to.trackorder_findByWorkOrderGid(self.track_query_data)
        trackList = resp.pop('data')
        print('trackList：', trackList)

        # 验证派工单生成数量为2
        self.assertEqual(2, len(trackList))


if __name__ == '__main__':
    unittest.main()
