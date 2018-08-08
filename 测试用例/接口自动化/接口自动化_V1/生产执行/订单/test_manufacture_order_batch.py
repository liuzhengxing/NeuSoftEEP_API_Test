# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_batch
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create


class OrderBatch(unittest.TestCase):
    u"""订单分单接口"""
    def setUp(self):
        self.ordergids = []
        for i in range(1):
            data = lcl_data_order('OrderCreate', 2)
            data['planQty'] = '10'
            req = order_create(data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)

    def test_order_batch_true(self):
        """订单正确分单"""
        gid = self.ordergids[0]
        blist = [2, 2, 2, 4]
        try:
            req = order_batch(gid, blist)
            print('订单正确分单', req)
            self.assertIn('data', json.loads(req))
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
