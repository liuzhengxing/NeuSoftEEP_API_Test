# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1 import lcl_data_workorder
from 测试用例.接口自动化.接口自动化_V1 import wobom_allot
from 测试用例.接口自动化.接口自动化_V1 import workorder_create

SheetName = 'WorkOrderCreate'


class WorkOrderBomAllot(unittest.TestCase):
    """自动关联工单bom接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            wodata = lcl_data_workorder(SheetName, 2)
            res = workorder_create(wodata)
            wogid = json.loads(res)['data']
            self.wogidlist.append(wogid)

    def test_manufacture_wobom_allot(self):
        """自动关联工单bom"""
        wogidlist = self.wogidlist[:1]
        try:
            req = wobom_allot(wogidlist)
            print('自动关联工单bom', req)
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
