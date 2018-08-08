# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化_V1.生产执行.订单BOM.orderbom_public import orderbom_manual
from 测试用例.接口自动化_V1.生产执行.订单BOM.orderbom_public import orderbom_query

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create

SheetName = 'OrderCreate'


class WorkOrderBomQuery(unittest.TestCase):
    """订单bom查询接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            wodata = lcl_data_order(SheetName, 2)
            res = order_create(wodata)
            wogid = json.loads(res)['data']
            self.wogidlist.append(wogid)

    def test_manufacture_wobom_manual(self):
        """订询工单bom"""
        wogid = self.wogidlist[0]
        print(wogid)
        try:
            orderbom_manual(wogid)
            req = orderbom_query(wogid)
            print('查询订单bom', req)
            assert len(json.loads(req)['data']) == 1, '查询到的数量错误'
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
