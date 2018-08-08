# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单 import order_public

SheetName = 'OrderCreate'
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class Test(unittest.TestCase):
    def setUp(self):
        self.ordergids = []
        for i in range(2):
            data = order_public.get_data(SheetName, 0, 1)
            data['planQty'] = 10
            req = order_public.order_create(**data)
            ordergid = json.loads(req)['data']
            self.ordergids.append(ordergid)

    def test_order(self):
        gidlist = self.ordergids
        gidlist.append('23232132143123')
        print('========', gidlist)
        # noinspection PyBroadException
        try:
            req = order_public.order_merge(gidlist)
            print('订单列表包含不存在的订单gid进行合单', req)
            assert json.loads(req)['message'] == '传入的订单gid集合包含不存在数据,请检查数据!'
        except Exception:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
