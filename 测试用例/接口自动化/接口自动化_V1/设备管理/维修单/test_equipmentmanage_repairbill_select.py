# _*_ coding: utf-8 _*_

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import repairbill_public


class RepairBillFind(unittest.TestCase):
    u'''维修单查询'''
    def setUp(self):
        pass

    def test_repairbill_findbykey(self):
        u'''按条件查询维修单'''
        rbfreq = repairbill_public.repairbill_find('')
        if 'data":' in rbfreq and 'pager":' in rbfreq and 'success":true' in rbfreq:
            assert 1 == 1
        else:
            assert 1 == 2
