#encoding = 'utf-8'
"""质检工单参照生成"""
import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.工单 import WorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params

class qualityWorkOrderRef(unittest.TestCase):
    """质检工单参照生成"""

    def setUp(self):
        self.wo = WorkOrder()
        self.qwo = QualityWorkOrder()
        self.workOrder_mock_data = {
            "code": pm.create_code(),
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

        self.workOrder_Rule_data = {
            "gid": "712E1C21843F5B4FE055000000000001",
            "name": "是否下发",
            "code": "IS_PUBLISH",
            "description": "是否下发",
            "activeRule": "false"
}


    def test_qualityWorkOrderRef(self):

        self.qwo.qualityWorkOrder_rule(self.workOrder_Rule_data)
        """派检规则 - 是否下发配置为否"""

        resp = self.wo.workorder_create(self.workOrder_mock_data)
        """创建工单，并生成gid"""

        gid_lists = [resp.pop("data")]

        # gid_lists = gid_list.append()
        print(gid_lists)

        self.wo.workorder_changeStatut(gid_lists)
        """工单下发"""

        status = self.qwo.qualityWorkOrder_ref(gid_lists)
        """参照生成质检工单"""

        print(self.workOrder_mock_data["code"])
        print(self.workOrder_mock_data["code"])



if __name__ == '__main__':
    unittest.main()