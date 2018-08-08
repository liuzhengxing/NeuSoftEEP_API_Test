# _*_ coding: utf-8 _*_

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulbill_public


class OverhaulBillSelect(unittest.TestCase):
    def setUp(self):
        pass

    def test_overhaulbill_select(self):
        u'''查询大修单详情'''
        obgid = overhaulbill_public.overhaulbill_create()
        obsreq = overhaulbill_public.overhaulbill_select(obgid)
        if obgid in obsreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_overhaulbill_find(self):
        u'''查询大修单列表'''
        obfreq = overhaulbill_public.overhaulbill_findbycode('')
        if 'data":' in obfreq and 'pager":' in obfreq and 'success":true' in obfreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
