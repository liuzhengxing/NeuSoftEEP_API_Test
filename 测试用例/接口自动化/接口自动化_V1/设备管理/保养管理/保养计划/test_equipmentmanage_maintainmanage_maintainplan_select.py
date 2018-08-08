# _*_coding: utf-8 _*_

import unittest

import requests

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import maintainplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class MaintainPlanSelect(unittest.TestCase):
    u'''保养计划查询'''
    def setUp(self):
        pass

    def test_maintainplan_detailselect(self):
        u'''保养计划详情查询'''
        # 创建保养计划
        mgid = maintainplan_public.maintainplan_create()
        # print(mgid)
        sreq = maintainplan_public.maintainplan_select(mgid)
        print(sreq)
        if mgid in sreq:
            assert 1 == 1
        else:
            assert 1 == 2


    def test_maintainplan_listselect(self):
        u'''保养计划列表查询'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainPlan/query.action'
        sreq = requests.get(interfaceurl, headers=headers).content.decode()
        if '"data":' in sreq and '"success":true' in sreq and '"pager":' in sreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
