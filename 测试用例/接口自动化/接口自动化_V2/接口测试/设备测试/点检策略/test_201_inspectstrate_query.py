# _*_ coding:utf-8 _*

import unittest

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy


class TestInspectStrategyQuery(unittest.TestCase):
    """点检策略查询测试类"""

    def setUp(self):
        self.isy = InspectStrategy()

        self.isy_add_data = [
            {
                "inspectCycle": 5,
                "inspectCycleUnit": "时",
                "bmEquipmentGid": params.bmEquipmentGid,
                "bmEquipInspectPartGid": params.bmEquipInspectPartGid,
                "bmEquipInspectItemGid": params.bmEquipInspectItemGid
            }
        ]

        self.isy_query_data = {
            "query": {
                "query": [
                    {
                        "field": "bmEquipmentGid",
                        "type": "eq",
                        "value": params.bmEquipmentGid,
                        "operator": "and"
                    }
                ]
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

    def test_inspectstrategy_query_1(self):
        """
        点检策略列表查询
        :return:
        """
        self.isy.inspectstrategiy_addBatch = Mock(side_effect=self.isy.inspectstrategiy_addBatch)
        resp_isy_add = self.isy.inspectstrategiy_addBatch(self.isy_add_data)

        self.isy.inspectstrategiy_query = Mock(side_effect=self.isy.inspectstrategiy_query)
        resp_isy_query = self.isy.inspectstrategiy_query(self.isy_query_data)

        self.assertLess(0, len(resp_isy_query.get('data')))


if __name__ == "__main__":
    unittest.main()
