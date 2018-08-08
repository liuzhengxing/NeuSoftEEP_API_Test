# _*_ coding: utf-8 _*_

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulbill_public


class OverhaulBillRecord(unittest.TestCase):
    def setUp(self):
        pass

    def test_overhaulbill_record(self):
        u'''大修单报工'''
        obgids = []
        obgid = overhaulbill_public.overhaulbill_create()
        obgids.append(obgid)
        overhaulbill_public.overhaulbill_dispatch(obgids)
        overhaulbill_public.overhaulbill_saveorrecord(obgid, 'record')
        obsreq = overhaulbill_public.overhaulbill_select(obgid)
        if 'status":"30' in obsreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
