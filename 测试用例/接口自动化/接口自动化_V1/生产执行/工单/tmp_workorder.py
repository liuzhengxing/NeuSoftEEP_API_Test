# _*_coding: utf-8_*_

import unittest

from 测试用例.接口自动化_V1.生产执行.工单 import workorder_public

SheetName = 'WorkOrderCreate'


class WorkOrderCreate(unittest.TestCase):
    u"""工单创建接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(3):
            order_data = workorder_public.get_data(SheetName, 0, 1)
            order_data['factoryLineGid'] = 'dfe56cc26cbe43ee9d3fc5054aeae603'
            wogid = workorder_public.workorder_create(**order_data)
            self.wogidlist.append(wogid)

    def test_workorder(self):
        """sssssssss"""
        try:
            wogidlist = self.wogidlist[:3]
            req = workorder_public.workorder_savesort('dfe56cc26cbe43ee9d3fc5054aeae603', wogidlist)
            print('sssssssss', req)
            # self.assertIn('success', req)
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
