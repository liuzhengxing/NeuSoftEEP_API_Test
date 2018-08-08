# _*_coding:utf-8_*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class OverhaulPlanDelete(unittest.TestCase):
    u'''大修单删除'''
    def setUp(self):
        pass

    def test_overhaulplan_delete_simple(self):
        u'''单个删除大修计划'''
        opgids = []
        opgid = overhaulplan_public.overhaulplan_create()
        opgids.append(opgid)
        overhaulplan_public.overhaulplan_delete(opgids)
        opsreq = overhaulplan_public.overhaulplan_select(opgid)
        if opgid not in opsreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_overhaulplan_delete_more(self):
        u'''批量删除大修计划'''
        opgids = []
        for c in range(3):
            opgid = overhaulplan_public.overhaulplan_create()
            opgids.append(opgid)
        overhaulplan_public.overhaulplan_delete(opgids)
        check = 0
        for opgid in opgids:
            opsreq = overhaulplan_public.overhaulplan_select(opgid)
            if opgid not in opsreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    # def test_overhaulplan_delete_uncreated(self):
    #     u'''删除非已创建状态的大修计划'''
    #     opgids = []
    #     opgid = overhaulplan_public.overhaulplan_create()
    #     opgids.append(opgid)
    #     equipmentmanage_public.associationequipment(opgid)
    #     overhaulplan_public.overhaulplan_senddown(opgids)
    #     opreq = overhaulplan_public.overhaulplan_delete(opgids)


if __name__ == '__main__':
    unittest.main()
