# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_changestatut
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create


class OrderChangeStatus(unittest.TestCase):
    u"""订单状态修改接口"""
    def setUp(self):
        self.ordergids = []
        for i in range(5):
            data = lcl_data_order('OrderCreate', 2)
            req = order_create(data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)

    def test_order_changestatus_one(self):
        """单条订单修改状态"""
        gids = self.ordergids[:1]
        # noinspection PyBroadException
        try:
            req = order_changestatut(gids)
            print('单条修改状态', req)
            assert json.loads(req)['success'] is True
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    def test_order_changestatus_more(self):
        """多条订单修改状态"""
        gids = self.ordergids[1:]
        # noinspection PyBroadException
        try:
            req = order_changestatut(gids)
            print('多条订单修改状态', req)
            assert json.loads(req)['success'] is True
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    # def test_order_changestatus_err(self):
    #     """不存在的订单修改状态"""
    #     gids = ['fdsaf23rda']
    #     # noinspection PyBroadException
    #     try:
    #         req = order_changestatut(gids)
    #         print('多条订单修改状态', req)
    #         assert json.loads(req)['message'] == '没有找到订单数据'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main()
