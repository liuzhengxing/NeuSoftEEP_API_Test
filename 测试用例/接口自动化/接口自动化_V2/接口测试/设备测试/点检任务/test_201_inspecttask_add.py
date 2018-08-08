# _*_ coding:utf-8 _*

import unittest

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检任务 import InspectTask


class TestInspectTaskAdd(unittest.TestCase):
    """点检任务创建测试类"""

    def setUp(self):
        self.isy = InspectStrategy()
        self.it = InspectTask()

        self.it_add_data = {
            "code": "001",
            "inspectTime": "2018-07-24 11:18:35",
            "bmEquipmentGid": params.bmEquipmentGid,
            "bmEquipInspectItemGid": params.bmEquipInspectItemGid,
            "bmEquipInspectPartGid": params.bmEquipInspectPartGid
        }

    def test_inspecttask_add_1(self):
        """
        点检任务创建
        :return:
        """
        code = create_code()

        self.it_add_data['code'] = code
        self.it.inspecttask_add = Mock(side_effect=self.it.inspecttask_add)
        resp_it_add = self.it.inspecttask_add(self.it_add_data)

        self.assertIn('data', resp_it_add.keys())


if __name__ == "__main__":
    unittest.main()
