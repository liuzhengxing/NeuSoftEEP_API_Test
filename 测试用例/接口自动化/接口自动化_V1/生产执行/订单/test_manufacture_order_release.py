# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_release


class OrderRelease(unittest.TestCase):
    u"""订单下发接口"""
    def setUp(self):
        self.ordergids = []
        for i in range(5):
            data = lcl_data_order('OrderCreate', 2)
            data['planQty'] = 10
            print(data)
            req = order_create(data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)

    def test_order_batch_one(self):
        """单条订单下发"""
        gidlist = self.ordergids[:1]
        # noinspection PyBroadException
        try:
            res = order_release(gidlist)
            print('单条订单下发', res)
            assert len(json.loads(res)['data']) == 10
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    def test_order_batch_more(self):
        """多条订单下发"""
        gidlist = self.ordergids[1:3]
        # noinspection PyBroadException
        try:
            res = order_release(gidlist)
            print('多条订单下发', res)
            assert len(json.loads(res)['data']) == 20
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    # def test_order_batch_none(self):
    #     """空订单下发"""
    #     gidlist = []
    #     # noinspection PyBroadException
    #     try:
    #         res = order_release(gidlist)
    #         print('空订单下发', res)
    #         assert json.loads(res)['message'] == '没有找到订单数据'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_batch_haswrong(self):
    #     """订单包含错误gid下发"""
    #     gidlist = self.ordergids
    #     gidlist.append('fdsafawerafwef')
    #     # noinspection PyBroadException
    #     try:
    #         res = order_release(gidlist)
    #         print('订单包含错误gid下发', res)
    #         assert json.loads(res)['message'] == '没有找到订单数据'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main()
