# -*- coding: utf-8 -*-

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulbill_public


class OverhaulBillDispatch(unittest.TestCase):
    def setUp(self):
        pass

    def test_overhaulbill_dispatch_simple(self):
        u'''单个大修单派工'''
        obgids = []
        obgid = overhaulbill_public.overhaulbill_create()
        obgids.append(obgid)
        overhaulbill_public.overhaulbill_dispatch(obgids)
        obsreq = overhaulbill_public.overhaulbill_select(obgid)
        if obgid in obsreq and 'status":"20' in obsreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_overhaulbill_dispatch_more(self):
        u'''大修单批量派工'''
        obgids = []
        for c in range(3):
            obgid = overhaulbill_public.overhaulbill_create()
            obgids.append(obgid)
        overhaulbill_public.overhaulbill_dispatch(obgids)
        check = 0
        for obgid in obgids:
            obsreq = overhaulbill_public.overhaulbill_select(obgid)
            if obgid in obsreq and 'status":"20' in obsreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_overhaulbill_dispatch_recorded(self):
        u'''已报工的大修单进行派工'''
        obgids = []
        obgid = overhaulbill_public.overhaulbill_create()
        obgids.append(obgid)
        overhaulbill_public.overhaulbill_dispatch(obgids)
        overhaulbill_public.overhaulbill_saveorrecord(obgid, 'record')
        obdpreq = overhaulbill_public.overhaulbill_dispatch(obgids)
        if 'message":"只有已创建的大修单才能派工' in obdpreq:
            assert 1 == 1
        else:
            assert 1 == 2
