# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import equipmentmanage_public
from 测试用例.接口自动化.接口自动化_V1.设备管理 import maintainplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class MaintainPlanSenddown(unittest.TestCase):
    u'''保养计划发布'''
    def setUp(self):
        pass

    def test_maintainplan_senddown_simple(self):
        u'''单条发布保养计划'''
        mgids = []
        mgid = maintainplan_public.maintainplan_create()
        mgids.append(mgid)
        equipmentmanage_public.associationequipment(mgid)
        maintainplan_public.maintainplan_senddown(mgids)
        sreq = maintainplan_public.maintainplan_select(mgid)
        # print(sreq)
        if '"status":"20"' in sreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_maintainplan_senddown_more(self):
        u'''批量发布保养计划'''
        mgids = []
        # 创建多条保养计划
        for c in range(3):
            mgid = maintainplan_public.maintainplan_create()
            mgids.append(mgid)
        # 逐个关联设备
        for mid in mgids:
            equipmentmanage_public.associationequipment(mid)
        # 批量发布
        maintainplan_public.maintainplan_senddown(mgids)
        # 验证发布
        check = 0
        for mid in mgids:
            sreq = maintainplan_public.maintainplan_select(mid)
            # print(sreq)
            if '"status":"20"' in sreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_maintainplan_senddown_again(self):
        u'''已发布的保养计划再次发布'''
        mgids = []
        mgid = maintainplan_public.maintainplan_create()
        mgids.append(mgid)
        equipmentmanage_public.associationequipment(mgid)
        maintainplan_public.maintainplan_senddown(mgids)
        dreq = maintainplan_public.maintainplan_senddown(mgids)
        # print(dreq)
        if 'message":"已经发布的保养单不能发布' in dreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
