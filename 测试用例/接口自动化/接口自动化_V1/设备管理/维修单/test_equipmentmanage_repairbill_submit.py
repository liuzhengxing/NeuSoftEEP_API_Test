# _*_ coding: utf-8 _*_

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import repairbill_public


class RepairBillSubmit(unittest.TestCase):
    u'''维修单提交'''
    def setUp(self):
        pass

    def test_repairbill_submit_simple(self):
        u'''单个维修单提交'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        rbsreq = repairbill_public.repairbill_select(rbgid)
        if 'status":"20' in rbsreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_repairbill_submit_more(self):
        u'''维修单批量提交'''
        rbgids = []
        for c in range(3):
            rbgid = repairbill_public.repairbill_create()
            rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        check = 0
        for rbgid in rbgids:
            rbsreq = repairbill_public.repairbill_select(rbgid)
            if 'status":"20' in rbsreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    # def test_repairbill_dispatch_dispatched(self):
    #     u'''已派工的维修单提交'''
    #     u'''单个维修单提交'''
    #     rbgids = []
    #     rbgid = repairbill_public.repairbill_create()
    #     rbgids.append(rbgid)
    #     repairbill_public.repairbill_submit(rbgids)
    #     repairbill_public.repairbill_dispatch(rbgids)
    #     rbsreq = repairbill_public.repairbill_submit(rbgids)
    #     if 'status":"20' in rbsreq:
    #         assert 1 == 1
    #     else:
    #         assert 1 == 2

    # def test_repairbill_dispatch_recorded(self):
    #     u'''已报工的维修单提交'''
    #     rbgids = []
    #     rbgid = repairbill_public.repairbill_create()
    #     rbgids.append(rbgid)
    #     repairbill_public.repairbill_submit(rbgids)
    #     repairbill_public.repairbill_dispatch(rbgids)
    #     repairbill_public.repairbill_saveorrecord(rbgid, 'record')
    #     rbsreq = repairbill_public.repairbill_submit(rbgids)
    #     if 'status":"20' in rbsreq:
    #         assert 1 == 1
    #     else:
    #         assert 1 == 2