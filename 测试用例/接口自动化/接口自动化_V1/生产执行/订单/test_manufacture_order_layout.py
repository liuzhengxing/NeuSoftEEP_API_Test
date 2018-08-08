# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_layout


class OrderLayOut(unittest.TestCase):
    u"""订单编排预览接口"""
    def setUp(self):
        self.ordergids = []
        for i in range(2):
            data = lcl_data_order('OrderCreate', 2)
            req = order_create(data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)

    def test_order_layout_true(self):
        u"""正常编排预览"""
        # noinspection PyBroadException
        try:
            req = order_layout(self.ordergids)
            print('正常编排预览', req)
            assert len(json.loads(req)['data']) == len(self.ordergids)
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    # def test_order_layout_noneorder(self):
    #     u"""不存在订单编排预览"""
    #     thisordergids = ['234efawfasfd', 'fdsafsdafd']
    #     # noinspection PyBroadException
    #     try:
    #         req = order_layout(thisordergids)
    #         print('不存在订单编排预览', req)
    #         assert req == ''
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_layout(self):
    #     u"""存在错误订单gid编排预览"""
    #     gidlist = self.ordergids
    #     gidlist.append('234efawfasfd')
    #     # noinspection PyBroadException
    #     try:
    #         req = order_layout(gidlist)
    #         print('存在错误订单gid编排预览', req)
    #         assert len(json.loads(req)['data']) == 10
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main()
