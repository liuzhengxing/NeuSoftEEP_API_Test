# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_merge


class OrderMerge(unittest.TestCase):
    u"""订单合单接口"""
    def setUp(self):
        self.ordergids = []
        for i in range(5):
            data = lcl_data_order('OrderCreate', 2)
            req = order_create(data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)

    # def test_order_merge_one(self):
    #     """单个订单合单"""
    #     gidlist = self.ordergids[:1]
    #     # noinspection PyBroadException
    #     try:
    #         req = order_merge(gidlist)
    #         print('单订单合单', req)
    #         self.assertIn('传入的订单数量小于最小合单数量', json.loads(req))
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2

    def test_order_merge_more(self):
        """多个订单合单"""
        gidlist = self.ordergids[1:3]
        # noinspection PyBroadException
        try:
            req = order_merge(gidlist)
            print('单订单合单', req)
            self.assertIn('SPO', json.loads(req)['data'])
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    # def test_order_merge_haserr(self):
    #     """订单列表包含不存在的订单gid进行合单"""
    #     gidlist = self.ordergids[3:]
    #     gidlist.append('23232132143123')
    #     # noinspection PyBroadException
    #     try:
    #         req = order_merge(gidlist)
    #         print('订单列表包含不存在的订单gid进行合单', req)
    #         assert json.loads(req)['message'] == '传入的订单gid集合包含不存在数据,请检查数据!'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_merge_allrr(self):
    #     """订单列表全部非法进行合单"""
    #     gidlist = ['3232323223', '32323232fvdfs']
    #     # noinspection PyBroadException
    #     try:
    #         req = order_merge(gidlist)
    #         print('订单列表全部非法进行合单', req)
    #         assert json.loads(req)['message'] == '传入的订单gid集合不存在,请检查数据!'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_merge_none(self):
    #     """订单列表为空进行合单"""
    #     gidlist = []
    #     # noinspection PyBroadException
    #     try:
    #         req = order_merge(gidlist)
    #         print('订单列表全部非法进行合单', req)
    #         assert json.loads(req)['message'] == '合单订单所传入的gid为空,请检查数据!'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main()
