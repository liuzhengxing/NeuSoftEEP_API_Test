# _*_ coding: utf-8 _*_

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import repairbill_public


class RepairBillDispatch(unittest.TestCase):
    u'''维修单派工'''
    def setUp(self):
        pass

    def test_repairbill_dispatch_simple(self):
        u'''单个维修单派工'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        repairbill_public.repairbill_dispatch(rbgids)
        rbsreq = repairbill_public.repairbill_select(rbgid)
        if 'status":"30' in rbsreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_repairbill_dispatch_more(self):
        u'''维修单批量派工'''
        rbgids = []
        for c in range(3):
            rbgid = repairbill_public.repairbill_create()
            rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        repairbill_public.repairbill_dispatch(rbgids)
        check = 0
        for rbgid in rbgids:
            rbsreq = repairbill_public.repairbill_select(rbgid)
            if 'status":"30' in rbsreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_repairbill_dispatch_created(self):
        u'''已创建的维修单直接派工'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        rbdpreq = repairbill_public.repairbill_dispatch(rbgids)
        if 'message":"无可派工维修单信息' in rbdpreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_repairbill_dispatch_dispatched(self):
        u'''已派工的维修单再次派工'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        repairbill_public.repairbill_dispatch(rbgids)
        rbdpreq = repairbill_public.repairbill_dispatch(rbgids)
        if 'message":"无可派工维修单信息' in rbdpreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_repairbill_dispatch_recorded(self):
        u'''已报工的维修单派工'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        repairbill_public.repairbill_dispatch(rbgids)
        repairbill_public.repairbill_saveorrecord(rbgid, 'record')
        rbdpreq = repairbill_public.repairbill_dispatch(rbgids)
        if 'message":"无可派工维修单信息' in rbdpreq:
            assert 1 == 1
        else:
            assert 1 == 2
