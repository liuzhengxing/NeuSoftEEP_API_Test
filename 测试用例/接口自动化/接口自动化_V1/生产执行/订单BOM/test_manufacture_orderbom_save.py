# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化_V1.生产执行.订单BOM.orderbom_public import orderbom_manual

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create

SheetName = 'OrderCreate'


class OrderBomSave(unittest.TestCase):
    """手动关联订单bom接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            wodata = lcl_data_order(SheetName, 2)
            res = order_create(wodata)
            wogid = json.loads(res)['data']
            self.wogidlist.append(wogid)

    def test_manufacture_wobom_manual(self):
        """手动关联订单bom"""
        wogid = self.wogidlist[0]
        try:
            req = orderbom_manual(wogid)
            print('手动关联订单bom', req)
            self.assertIn('data', json.loads(req))
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()