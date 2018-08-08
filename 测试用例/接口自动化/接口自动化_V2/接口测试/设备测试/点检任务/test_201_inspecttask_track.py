# _*_ coding:utf-8 _*

import unittest

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检任务 import InspectTask


class TestInspectTaskTrack(unittest.TestCase):
    """点检任务批量派工测试类"""

    def setUp(self):
        self.it = InspectTask()

        self.it_addf_data = {
            "bmEquipmentGid": params.bmEquipmentGid,
            "beginTime": "2017-12-31 11:18:35",
            "endTime": "2018-01-01 11:18:35"
        }
        self.it_track_data = {
            "gids": [],
            "headPersonnelGid": params.smPersonnelGid
        }

    def test_inspecttask_track_1(self):
        """
        点检任务创建
        :return:
        """
        self.it.inspecttask_addFromInspectStrategy = Mock(side_effect=self.it.inspecttask_addFromInspectStrategy)
        resp_it_addf = self.it.inspecttask_addFromInspectStrategy(self.it_addf_data)

        it_list = resp_it_addf.get('data')
        self.it_track_data['gids'] = it_list

        self.it.inspecttask_track = Mock(side_effect=self.it.inspecttask_track)
        resp_it_track = self.it.inspecttask_track(self.it_track_data)

        self.assertIn('success', resp_it_track.keys())


if __name__ == "__main__":
    unittest.main()
