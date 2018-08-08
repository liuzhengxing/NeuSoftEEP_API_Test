# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_modify


class OrderModify(unittest.TestCase):
    u"""订单修改接口"""
    def setUp(self):
        self.ordergids = []
        for i in range(1):
            data = lcl_data_order('OrderCreate', 2)
            req = order_create(data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)

    def test_order_batch_true(self):
        """订单修改计划数量"""
        gid = self.ordergids[0]
        try:
            args = lcl_data_order('OrderCreate', 2)
            args['gid'] = gid
            args['planQty'] = 20
            req = order_modify(args)
            print('订单修改计划数量', req)
            self.assertIn('success', json.loads(req))
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
