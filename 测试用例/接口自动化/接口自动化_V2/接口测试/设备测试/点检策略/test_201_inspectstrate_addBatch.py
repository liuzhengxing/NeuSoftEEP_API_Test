# _*_ coding:utf-8 _*

import unittest

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy


class TestInspectStrategyAdd(unittest.TestCase):
    """点检策略创建测试类"""

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

    def test_inspectstrategy_addBatch_1(self):
        """
        点检策略创建
        :return:
        """
        self.isy.inspectstrategiy_addBatch = Mock(side_effect=self.isy.inspectstrategiy_addBatch)
        resp_isy_add = self.isy.inspectstrategiy_addBatch(self.isy_add_data)
        print('Respones：', resp_isy_add)
        self.assertIn('data', resp_isy_add.keys())


if __name__ == "__main__":
    unittest.main()
