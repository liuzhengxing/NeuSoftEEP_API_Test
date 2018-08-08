# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化_V1.生产执行.订单工艺.orderroute_public import orderroute_manule

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create

SheetName = 'OrderCreate'


class OrderRouteSave(unittest.TestCase):
    """订单手动关联工艺接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            wodata = lcl_data_order(SheetName, 2)
            res = order_create(wodata)
            wogid = json.loads(res)['data']
            self.wogidlist.append(wogid)

    def test_manufacture_woroute_manual(self):
        """订单手动关联工艺"""
        ordergid = self.wogidlist[0]
        try:
            req = orderroute_manule(ordergid)
            print('订单手动关联工艺', req)
            self.assertIn('data', json.loads(req))
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
