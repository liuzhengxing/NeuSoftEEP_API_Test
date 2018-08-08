# _*_ coding: utf-8 _*_

import unittest

from 测试用例.接口自动化.接口自动化_V1.设备管理 import repairbill_public


class RepairBillCreate(unittest.TestCase):
    u'''维修单创建'''
    def setUp(self):
        pass

    def test_repairbill_create(self):
        u'''创建维修单并查询详情'''
        rbgid = repairbill_public.repairbill_create()
        rbs = repairbill_public.repairbill_select(rbgid)
        if rbgid in rbs:
            assert 1 == 1
        else:
            assert 1 == 2