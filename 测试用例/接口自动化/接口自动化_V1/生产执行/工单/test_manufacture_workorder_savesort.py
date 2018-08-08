# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1 import lcl_data_workorder
from 测试用例.接口自动化.接口自动化_V1 import workorder_create
from 测试用例.接口自动化.接口自动化_V1 import workorder_savesort
from 测试用例.接口自动化.接口自动化_V1 import woroute_manule

SheetName = 'WorkOrderCreate'


class WorkOrderSaveSort(unittest.TestCase):
    u"""工单编排保存接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(2):
            data = lcl_data_workorder(SheetName, 2)
            data['planQty'] = i+1
            res = workorder_create(data)
            wogid = json.loads(res)['data']
            woroute_manule(wogid)
            self.wogidlist.append(wogid)

    def test_workorder_savesort_true(self):
        """工单正常编排保存"""
        try:
            flgid = 'dfe56cc26cbe43ee9d3fc5054aeae603'
            wogidlist = self.wogidlist

            req = workorder_savesort(flgid, wogidlist)
            print('工单正常编排保存', req)
            self.assertIn('success', json.loads(req))
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
