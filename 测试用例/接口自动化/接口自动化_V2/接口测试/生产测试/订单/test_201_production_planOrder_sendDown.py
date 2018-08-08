# _*_ coding:utf-8 _*_

import unittest

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.订单 import PlanOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from public import params


class TestPlanOrderSendDown(unittest.TestCase):
    """订单下发测试类"""

    def setUp(self):
        self.po = PlanOrder()
        self.planOrder_mock_data = {
            "code": "",
            "workCenterGid": params.bmFactoryWorkCenterGid,
            "orderType": "62DC90DAFA845CB2E055000000000001",
            "materialGid": params.MaterielSJGid,
            "materialVersion": "1",
            "planBeginTime": "2018-05-04",
            "planEndTime": "2018-05-14",
            "planQty": 10,
            "finishQty": "",
            "publishedQty": "",
            "qualifiedQty": "",
            "unqualifiedQty": "",
            "wasteQty": "",
            "orderStatus": "",
            "planOrderSource": "",
            "planOrderCategory": "normal",
            "factoryLineGid": params.bmFactoryLineCF,
            "actualBeginTime": "",
            "actualEndTime": "",
            "measureBeginTime": "",
            "measureEndTime": "",
            "bomStatus": "",
            "processStatus": "",
            "canOperation": "",
            "surplusOrderFlag": ""
        }

    def test_planorder_senddown_1(self):
        """订单下发接口测试：下发生产工单数量验证"""
        planOrderGidList = []

        # 订单创建
        code = "PO" + create_code()
        print('订单编码：', code)
        self.planOrder_mock_data['code'] = code
        self.po.planorder_create = Mock(side_effect=self.po.planorder_create)
        resp = self.po.planorder_create(self.planOrder_mock_data)

        planOrderGid = resp.pop('data')
        planOrderGidList.append(planOrderGid)

        # 订单下发
        self.po.planorder_release = Mock(side_effect=self.po.planorder_release)
        resp = self.po.planorder_release(planOrderGidList)

        print('Response：', resp)

        # 验证生成工单数量为1
        self.assertEqual(1, len(resp.pop('data')))

    def test_planorder_senddown_2(self):
        """订单下发接口测试：下发生产工单回写生产订单已生成数量验证"""
        planOrderGidList = []

        # 订单创建
        code = "PO" + create_code()
        print('订单编码：', code)
        self.planOrder_mock_data['code'] = code
        self.po.planorder_create = Mock(side_effect=self.po.planorder_create)
        resp = self.po.planorder_create(self.planOrder_mock_data)

        planOrderGid = resp.pop('data')
        planOrderGidList.append(planOrderGid)

        # 订单下发
        self.po.planorder_release = Mock(side_effect=self.po.planorder_release)
        resp = self.po.planorder_release(planOrderGidList)

        print('Response：', resp)
        planOrderGid = resp.get('data')[0]

        # 订单查询
        self.po.planorder_findById = Mock(side_effect=self.po.planorder_findById)
        resp = self.po.planorder_findById(planOrderGid)

        print('Response：', resp)

        # 验证已下发数量为10
        self.assertEqual(10, resp.pop('data').pop('publishedQty'))


if __name__ == '__main__':
    unittest.main()
