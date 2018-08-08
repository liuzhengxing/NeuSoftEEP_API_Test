# _*_ coding:utf-8 _*

import unittest

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检任务 import InspectTask


class TestInspectTaskFindById(unittest.TestCase):
    """点检任务详情查询测试类"""

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

    def test_inspecttask_findById_1(self):
        """
        点检任务详情查询
        :return:
        """
        code = create_code()

        self.it_add_data['code'] = code
        self.it.inspecttask_add = Mock(side_effect=self.it.inspecttask_add)
        resp_it_add = self.it.inspecttask_add(self.it_add_data)

        it_gid = resp_it_add.get('data')

        self.it.inspecttask_findById = Mock(side_effect=self.it.inspecttask_findById)
        resp_it_find = self.it.inspecttask_findById(it_gid)
        self.assertIn('code', resp_it_find.get('data').keys())


if __name__ == "__main__":
    unittest.main()
