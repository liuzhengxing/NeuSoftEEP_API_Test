import unittest

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.订单 import PlanOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.工单 import WorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from public import params


class TestWorkOrderCreate(unittest.TestCase):
    """工单创建测试类"""

    def setUp(self):
        self.po = PlanOrder()
        self.wo = WorkOrder()
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
        self.workOrder_mock_data = {
            "code": "",
            "resourceOrderGid": "",
            "materialGid": params.MaterielSJGid,
            "orderType": "62DC90DAFA845CB2E055000000000001",
            "workCenterGid": params.bmFactoryWorkCenterGid,
            "factoryLineGid": params.bmFactoryLineCF,
            "routeLineGid": "",
            "planQty": 10,
            "planBeginTime": "2018-05-01",
            "planEndTime": "2018-05-31",
            "actualBeginTime": "",
            "actualEndTime": "",
            "finishQty": "",
            "measureBeginTime": "",
            "measureEndTime": "",
            "orderSeq": "",
            "parentWorkOrderGid": "",
            "freezeStatus": "",
            "orderStatus": "",
            "bomStatus": "",
            "createStatus": "",
            "roundNum": "",
            "processStatus": "",
            "createKmFlag": "",
            "createQacFlag": "",
            "repairCardGid": "",
            "measurementUnitGid": params.bmMeasurementUnitGid,
            "materialVersion": "1",
            "busiActivityType": "",
            "qualifiedQty": "",
            "unqualifiedQty": "",
            "wasteQty": "",
            "batchNumber": "",
            "productGid": "",
            "workOrderCategory": "",
            "bomVersion": "",
            "routeLineVersion": "",
            "canOperation": "",
            "surplusOrderFlag": "",
            "publishedQty": "",
            "factoryLineType": "",
            "generatedCode": ""
        }

    def test_workorder_create_1(self):
        """工单参照生成接口测试：参照数量大于计划数量"""
        code = "PO" + create_code()
        print('订单编码：', code)
        self.planOrder_mock_data['code'] = code

        # 订单创建
        self.po.planorder_create = Mock(side_effect=self.po.planorder_create)
        resp = self.po.planorder_create(self.planOrder_mock_data)

        planOrderGidList = []
        planOrderGid = resp.pop('data')
        planOrderGidList.append(planOrderGid)

        # 订单下发修改状态
        self.po.planorder_changeStatut = Mock(side_effect=self.po.planorder_changeStatut)
        self.po.planorder_changeStatut(planOrderGidList)

        # 工单参照订单生成
        insertBy_mock_data = [
            {
                "gid": planOrderGid,
                "refCreateQty": 11
            }
        ]
        self.wo.workorder_insertByPlanOrder = Mock(side_effect=self.wo.workorder_insertByPlanOrder)
        resp = self.wo.workorder_insertByPlanOrder(insertBy_mock_data)
        print('Response：', resp)

        # 验证异常码为105000
        self.assertEqual(105000, resp.pop('code'))

    def test_workorder_create_2(self):
        """工单创建接口测试：自动编码"""

        self.wo.workorder_create = Mock(side_effect=self.wo.workorder_create)
        resp = self.wo.workorder_create(self.workOrder_mock_data)
        print('Response：', resp)

        # 验证GID存在
        self.assertIn('data', resp.keys())


if __name__ == '__main__':
    unittest.main()
