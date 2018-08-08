# _*_ coding:utf-8 _*_

import unittest
import json

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口测试.测试套件.生产工单下发 import workorder_changestatus
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物料需求 import MaterialRequirement
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物流单 import Logistics
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物流单报工 import LogBillReport
from public import params


class TestMaterialeRequirementWareHouse(unittest.TestCase):
    """物料需求分配仓库测试类"""

    def setUp(self):
        self.mr = MaterialRequirement()
        self.lg = Logistics()
        self.lbr = LogBillReport()

        self.mr_create_data = {
            "uda2": "小米仓",
            "demandType": "WAREHOUSE",
            "scheduleDate": "2018-07-15 10:51:11",
            "factoryStationRef": {
                "stationName": "CPU"
            },

            "code": "test",
            "delivery": "params.bmFactoryWorkStationCPUGid",     #
            "sourceType": "CREATE",
            "reqWarehouseGidRef": {
                "name": "小米仓"      #
            },
            "demandGid": params.bmWarehouseGid,
            "planDate": "2018-07-01 10:51:11",
            "smBusiUnitGidRef": {
                "busiUnitName": "小米科技"
            },
            "imeLogisticsMaterialRequirementDetailList": [
                {
                    "originalQty": "8",
                    "bmMeasurementUnitGidRef": {
                        "gid": params.bmMeasurementUnitGid
                    },
                    "factoryStationRef": {
                        "stationName": "CPU"
                    },
                    "factoryWorkStationGid": params.bmFactoryWorkStationCPUGid,
                    "demandQty": "8",
                    "materialRef": {
                        "code": "Q11",
                        "name": "处理器",
                        "bmMeasurementUnitGidRef": {
                            "name": "件"
                        }
                    },
                    "supplyWarehouseGid": params.bmWarehouseGid,
                    "warehouseRef": {
                        "name": "小米仓"
                    },
                    "eventPayload": {},
                    "materialGid": params.MaterielCPUGid
                }
            ],
            "smBusiUnitGid": params.busiUnitGid,
            "uda1": "Q1"
        }

        self.mr_mauwh_data = {
            "gids": [],
            "warehouseGid": params.bmWarehouseGid2
        }

        self.mr_query_data = {
            "query": {
                "query": [
                    {
                        "field": "code",
                        "type": "eq",
                        "value": "TB002420180427",
                        "operator": "and"
                    }
                ]
            }
        }

    def test_mrwh_manuallyWarehouse_1(self):
        """
        物料需求手工分配仓库
        :return:
        """
        code = create_code()
        self.mr_create_data['code'] = code
        self.mr.materialmrequirement_add = Mock(side_effect=self.mr.materialmrequirement_add)
        resp_mr_add = self.mr.materialmrequirement_add(self.mr_create_data)

        mr_gid_list = []
        mr_gid = resp_mr_add.get('data')
        mr_gid_list.append(mr_gid)

        self.mr_mauwh_data['gids'] = mr_gid_list
        self.mr.materialmrequirement_manuallyWarehouse = Mock(side_effect=self.mr.materialmrequirement_manuallyWarehouse)
        resp_mr_mauwh = self.mr.materialmrequirement_manuallyWarehouse(self.mr_mauwh_data)

        self.assertEqual(1, len(resp_mr_mauwh.get('data')))

    def test_mrwh_autoWarehouse_1(self):
        """
        物料需求按条件自动分配仓库
        :return:
        """
        code = create_code()
        self.mr_create_data['code'] = code
        self.mr.materialmrequirement_add = Mock(side_effect=self.mr.materialmrequirement_add)
        resp_mr_add = self.mr.materialmrequirement_add(self.mr_create_data)

        mr_gid = resp_mr_add.get('data')

        self.mr_query_data['query']['query'][0]['value'] = code
        self.mr.materialmrequirement_autoWarehouse = Mock(side_effect=self.mr.materialmrequirement_autoWarehouse)
        resp_mr_auwh = self.mr.materialmrequirement_autoWarehouse(self.mr_query_data)

        # 验证返回中的物料需求GID存在且为1
        self.assertEqual(1, len(resp_mr_auwh.get('data')))

    def test_mrwh_autoWarehouseBy_1(self):
        """
        物料需求按条件自动分配仓库
        :return:
        """
        code = create_code()
        self.mr_create_data['code'] = code
        self.mr.materialmrequirement_add = Mock(side_effect=self.mr.materialmrequirement_add)
        resp_mr_add = self.mr.materialmrequirement_add(self.mr_create_data)

        mr_gid_list = []
        mr_gid = resp_mr_add.get('data')
        mr_gid_list.append(mr_gid)

        self.mr_mauwh_data['gids'] = mr_gid_list
        self.mr.materialmrequirement_autoWarehouseByGid = Mock(
            side_effect=self.mr.materialmrequirement_autoWarehouseByGid)
        resp_mr_aubwh = self.mr.materialmrequirement_autoWarehouseByGid(mr_gid_list)

        self.assertEqual(1, len(resp_mr_aubwh.get('data')))


if __name__ == '__main__':
    unittest.main()
