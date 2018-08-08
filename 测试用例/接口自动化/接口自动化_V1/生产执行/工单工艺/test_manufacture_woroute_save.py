# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1 import lcl_data_workorder
from 测试用例.接口自动化.接口自动化_V1 import workorder_create
from 测试用例.接口自动化.接口自动化_V1 import woroute_manule

SheetName = 'WorkOrderCreate'


class WorkOrderRouteSave(unittest.TestCase):
    """工单手动关联工艺接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            wodata = lcl_data_workorder(SheetName, 2)
            res = workorder_create(wodata)
            wogid = json.loads(res)['data']
            self.wogidlist.append(wogid)

    def test_manufacture_woroute_manual(self):
        """工单手动关联工艺"""
        wogid = self.wogidlist[0]
        try:
            req = woroute_manule(wogid)
            print('工单手动关联工艺', req)
            self.assertIn('data', json.loads(req))
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
