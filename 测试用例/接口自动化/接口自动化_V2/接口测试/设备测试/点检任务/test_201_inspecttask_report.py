# _*_ coding:utf-8 _*

import unittest

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检任务 import InspectTask


class TestInspectTaskReport(unittest.TestCase):
    """点检任务报工测试类"""

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

        self.it_report_data = {
            "gid": "",
            "inspectResult": "normal",
            "inspectResultDescription": "设备运行正常",
            "reportPersonnelGid": params.smPersonnelGid
        }

    def test_inspecttask_report_1(self):
        """
        点检任务报工
        :return:
        """
        code = create_code()

        self.it_add_data['code'] = code
        self.it.inspecttask_addAndTrack = Mock(side_effect=self.it.inspecttask_addAndTrack)
        resp_it_adda = self.it.inspecttask_addAndTrack(self.it_add_data)

        it_gid = resp_it_adda.get('data')
        self.it_report_data['gid'] = it_gid

        self.it.inspecttask_report = Mock(side_effect=self.it.inspecttask_report)
        resp_it_report = self.it.inspecttask_report(self.it_report_data)
        self.assertIn('success', resp_it_report.keys())


if __name__ == "__main__":
    unittest.main()
