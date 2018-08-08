# _*_coding:utf-8_*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import equipmentmanage_public
from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class OverhaulPlanSenddown(unittest.TestCase):
    def setUp(self):
        pass

    def test_overhaulplan_senddown_simple(self):
        u'''发布单条大修计划'''
        opgids = []
        opgid = overhaulplan_public.overhaulplan_create()
        opgids.append(opgid)
        equipmentmanage_public.associationequipment(opgid)
        overhaulplan_public.overhaulplan_senddown(opgids)
        opsreq = overhaulplan_public.overhaulplan_select(opgid)
        if 'status":"20' in opsreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_overhaulplan_senddown_more(self):
        u'''批量发布大修计划'''
        opgids = []
        for c in range(3):
            opgid = overhaulplan_public.overhaulplan_create()
            opgids.append(opgid)
        for opgid in opgids:
            equipmentmanage_public.associationequipment(opgid)
        overhaulplan_public.overhaulplan_senddown(opgids)
        check = 0
        for opgid in opgids:
            opsreq = overhaulplan_public.overhaulplan_select(opgid)
            if 'status":"20' in opsreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_overhaulplan_delete_more(self):
        u'''发布非已创建状态的大修计划'''
        opgids = []
        opgid = overhaulplan_public.overhaulplan_create()
        opgids.append(opgid)
        equipmentmanage_public.associationequipment(opgid)
        overhaulplan_public.overhaulplan_senddown(opgids)
        opsdreq = overhaulplan_public.overhaulplan_senddown(opgids)
        if 'message":"已经发布的大修计划不能发布' in opsdreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
