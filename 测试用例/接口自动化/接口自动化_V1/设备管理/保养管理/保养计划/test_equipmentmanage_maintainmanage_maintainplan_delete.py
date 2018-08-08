# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import maintainplan_public

domain = params.testdomain
port = params.testport


class MaintainPlanCreate(unittest.TestCase):
    u'''保养计划删除'''
    def setUp(self):
        pass

    def test_maintainplan_delete_simple(self):
        u'''单个删除保养计划'''
        mgids = []
        maintainplangid = maintainplan_public.maintainplan_create()
        # print('======', maintainplangid)
        mgids.append(maintainplangid)

        # 删除操作
        maintainplan_public.maintainplan_delete(mgids)

        # 验证删除
        sreq = maintainplan_public.maintainplan_select(maintainplangid)
        # print(sreq)
        if maintainplangid not in sreq:
            assert 1 == 1
        else:
            assert 1 == 2


    def test_maintainplan_delete_more(self):
        u'''批量删除保养计划'''
        mgids = []
        for c in range(3):
            maintainplangid = maintainplan_public.maintainplan_create()
            # print('======', maintainplangid)
            mgids.append(maintainplangid)

        # 删除操作
        maintainplan_public.maintainplan_delete(mgids)

        # 验证删除
        check = 0
        for mgid in mgids:
            sreq = maintainplan_public.maintainplan_select(mgid)
            # print(sreq)
            if mgid not in sreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

'''
    def test_maintainplan_delete_uncreate(self):
        u删除非已创建状态的保养计划
        mgids = []
        maintainplangid = maintainplan_public.maintainplan_create()
        # print('======', maintainplangid)
        mgids.append(maintainplangid)

        # 关联设备
        equipmentmanage_public.associationequipment(maintainplangid)

        # 下发保养计划
        maintainplan_public.maintainplan_senddown(mgids)

        # 删除操作
        dreq = maintainplan_public.maintainplan_delete(mgids)
        print(dreq)
'''

if __name__ == '__main__':
    unittest.main()
