# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1 import lcl_data_workorder
from 测试用例.接口自动化.接口自动化_V1 import workorder_create
from 测试用例.接口自动化.接口自动化_V1 import workorder_modify


class OrderModify(unittest.TestCase):
    u"""工单修改接口"""
    def setUp(self):
        self.ordergids = []
        for i in range(1):
            data = lcl_data_workorder('WorkOrderCreate', 2)
            req = workorder_create(data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)
        # print(self.ordergids)

    def test_order_batch_true(self):
        """工单修改计划数量"""
        gid = self.ordergids[0]
        try:
            args = lcl_data_workorder('OrderCreate', 2)
            args['gid'] = gid
            args['planQty'] = 20
            args['factoryLineGid'] = 'dfe56cc26cbe43ee9d3fc5054aeae603'
            req = workorder_modify(args)
            print('工单修改计划数量', req)
            self.assertIn('success', json.loads(req))
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
