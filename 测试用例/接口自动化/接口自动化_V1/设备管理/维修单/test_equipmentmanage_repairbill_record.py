# _*_ coding: utf-8 _*_

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import repairbill_public


class RepairBillRecord(unittest.TestCase):
    u'''维修单报工'''
    def setUp(self):
        pass

    def test_repairbill_recode_simple(self):
        u'''单个维修单报工'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        repairbill_public.repairbill_dispatch(rbgids)
        repairbill_public.repairbill_saveorrecord(rbgid, 'record')
        rbdpreq = repairbill_public.repairbill_select(rbgid)
        if 'status":"40' in rbdpreq:
            assert 1 == 1
        else:
            assert 1 == 2

    # def test_repairbill_submit_created(self):
    #     u'''已创建的维修单报工'''
    #     rbgid = repairbill_public.repairbill_create()
    #     rrreq = repairbill_public.repairbill_saveorrecord(rbgid, 'record')
    #     if 'status":"40' in rrreq:
    #         assert 1 == 1
    #     else:
    #         assert 1 == 2


    # def test_repairbill_submit_submited(self):
    #     u'''已提交的维修单报工'''


    def test_repairbill_recode_recorded(self):
        u'''已报工的维修单再次报工'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        repairbill_public.repairbill_dispatch(rbgids)
        repairbill_public.repairbill_saveorrecord(rbgid, 'record')
        rbdpreq = repairbill_public.repairbill_saveorrecord(rbgid, 'record')
        if 'message":"已派工单据才可报工' in rbdpreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_repairbill_recode_save(self):
        u'''维修单报工时保存'''
        rbgids = []
        rbgid = repairbill_public.repairbill_create()
        rbgids.append(rbgid)
        repairbill_public.repairbill_submit(rbgids)
        repairbill_public.repairbill_dispatch(rbgids)
        repairbill_public.repairbill_saveorrecord(rbgid, 'save')
        rbsreq = repairbill_public.repairbill_select(rbgid)
        if 'status":"30' in rbsreq:
            assert 1 == 1
        else:
            assert 1 == 2
