# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化_V1.生产执行.工单.workorder_public import workorder_refecreaate

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create

SheetName = 'WorkOrderCreate'


class WorkOrderRefeCreate(unittest.TestCase):
    u"""参照订单生成工单接口"""
    def setUp(self):
        self.ordergidlist = []
        for i in range(1):
            order_data = lcl_data_order('OrderCreate', 2)
            order_data['planQty'] = 5
            order_data['factoryLineGid'] = 'dfe56cc26cbe43ee9d3fc5054aeae603'
            ordergid = json.loads(order_create(order_data))['data']
            self.ordergidlist.append(ordergid)

    def test_workorder_refecreate_true(self):
        u"""正常参照生成"""
        ordergid = self.ordergidlist[0]
        data = [{
                    "gid": ordergid,
                    "refCreateQty": 1
        }]
        # noinspection PyBroadException
        try:
            req = workorder_refecreaate(data)
            print('正常参照生成', req)
            self.assertIn('success', req)
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    # def test_workorder_refecreate_nofline(self):
    #     u"""无产线参照生成"""
    #     order_data = order_get_data('OrderCreate', 0, 1)
    #     ordergid = json.loads(order_create(**order_data))['data']
    #     data = [{
    #                 "gid": ordergid,
    #                 "refCreateQty": 1
    #     }]
    #     # noinspection PyBroadException
    #     try:
    #         req = workorder_refecreaate(data)
    #         print('无产线参照生成', req)
    #         self.assertIn('未指定产线的订单', req)
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_workorder_refecreate_err1(self):
    #     u"""参照生成数量大于计划数量"""
    #     ordergid = self.ordergidlist[1]
    #     data = [{
    #                 "gid": ordergid,
    #                 "refCreateQty": 6
    #     }]
    #     # noinspection PyBroadException
    #     try:
    #         req = workorder_refecreaate(data)
    #         print('参照生成数量大于计划数量', req)
    #         self.assertIn('参照生成数量不能大于订单未下发数量', req)
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main()
