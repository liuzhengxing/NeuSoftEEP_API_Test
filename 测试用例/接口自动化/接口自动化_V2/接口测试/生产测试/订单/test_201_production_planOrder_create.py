import unittest

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.订单 import PlanOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from public import params


class TestPlanOrderCreate(unittest.TestCase):
    """订单创建测试类"""

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

    def test_planorder_create_1(self):
        """订单创建接口测试：输入正确的必填项生成订单"""
        code = "PO" + create_code()
        print('订单编码：', code)
        self.planOrder_mock_data['code'] = code

        self.po.planorder_create = Mock(side_effect=self.po.planorder_create)
        resp = self.po.planorder_create(self.planOrder_mock_data)
        print('Response：', resp)

        # 验证订单GID存在
        self.assertIn('data', resp.keys())

    def test_planorder_create_2(self):
        """订单创建接口测试：自动编码"""
        self.planOrder_mock_data['code'] = ''

        self.po.planorder_create = Mock(side_effect=self.po.planorder_create)
        resp = self.po.planorder_create(self.planOrder_mock_data)
        print('Response：', resp)

        # 验证订单GID存在
        self.assertIn('data', resp.keys())


if __name__ == '__main__':
    unittest.main()
