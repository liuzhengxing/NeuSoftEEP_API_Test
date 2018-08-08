# _*_coding:utf-8_*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class OverhaulPlanSelect(unittest.TestCase):
    u'''大修计划查询'''
    def setUp(self):
        pass

    def test_overhaulplan_select_detail(self):
        u'''查询大修计划详情'''
        # 新建大修计划
        opgid = overhaulplan_public.overhaulplan_create()
        sreq = overhaulplan_public.overhaulplan_select(opgid)
        if opgid in sreq:
            assert 1 == 1
        else:
            assert 1 == 2

    # def test_overhaulplan_find(self):
    #     u'''按大修计划编号查询'''
    #     # 新建大修计划
    #     opgid = overhaulplan_public.overhaulplan_create()
    #     sreq = overhaulplan_public.overhaulplan_select(opgid)
    #     opcode = json.loads(sreq)['data']['code']
    #     opfreq = overhaulplan_public.iverhaulplan_find(opcode)
    #     if opcode in opfreq:
    #         assert 1 == 1
    #     else:
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main()
