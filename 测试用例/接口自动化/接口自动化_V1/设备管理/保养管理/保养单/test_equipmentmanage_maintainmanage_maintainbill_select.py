# _*_coding: utf-8 _*_

import unittest

import requests

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import maintainbill_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class MaintainBillSelect(unittest.TestCase):
    u'''保养单查询'''
    def setUp(self):
        pass

    def test_maintainbill_detailselect(self):
        u'''保养单详情查询'''
        # 获取保养单GID
        mbgid = maintainbill_public.maintainbill_create()
        # print(mbgid)
        # 查询保养单详情
        dreq = maintainbill_public.maintainbill_select(mbgid)
        # print(dreq)
        # 验证查询结果
        if mbgid in dreq:
            assert 1 == 1
        else:
            assert 1 == 2


    def test_maintainbill_listselect(self):
        u'''保养单列表查询'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainBill/query.action'
        sreq = requests.get(interfaceurl, headers=headers).content.decode()
        if '"data":' in sreq and '"success":true' in sreq and '"pager":' in sreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
