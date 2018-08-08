#encoding = 'utf-8'
"""质检工单删除"""
import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params

class qualityWorkOrderDel(unittest.TestCase):
    """质检工单删除"""

    def setUp(self):

        self.qwo = QualityWorkOrder()
        self.qualityWorkOrder_data = {
            "smBusiUnitGid": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
            "code": pm.create_code(),
            "mdMaterialGid": params.MaterielSJGid,
            "shouldCheckQty": 10
        }

        resp1 = self.qwo.qualityWorkOrder_create(self.qualityWorkOrder_data)
        # print(resp1)
        # 直接创建一条质检工单

        self.qualityWorkOrderDel_data = [resp1.pop("data")]


    def test_qualityWorkOrderRef(self):
        resp2 = self.qwo.qualityWorkOrder_delete(self.qualityWorkOrderDel_data)
        print(resp2)
        self.assertEqual(True,resp2.pop("success"))

if __name__ == '__main__':
    unittest.main()