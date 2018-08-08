# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1 import lcl_data_workorder
from 测试用例.接口自动化.接口自动化_V1 import wobom_manual
from 测试用例.接口自动化.接口自动化_V1 import workorder_create
from 测试用例.接口自动化.接口自动化_V1 import workorder_release
from 测试用例.接口自动化.接口自动化_V1 import woroute_manule

SheetName = 'WorkOrderCreate'


class WorkOrderRelease(unittest.TestCase):
    u"""工单下发生成派工单接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            order_data = lcl_data_workorder(SheetName, 2)
            order_data['factoryLineGid'] = 'dfe56cc26cbe43ee9d3fc5054aeae603'
            req = workorder_create(order_data)
            wogid = json.loads(req)['data']
            self.wogidlist.append(wogid)

    def test_workorder_release_true(self):
        """工单下发"""
        try:
            wogidlist = self.wogidlist
            wogid = wogidlist[0]
            wobom_manual(wogid)
            woroute_manule(wogid)
            req = workorder_release(wogidlist)
            print('工单下发', req)
            self.assertIn('success', json.loads(req))
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
