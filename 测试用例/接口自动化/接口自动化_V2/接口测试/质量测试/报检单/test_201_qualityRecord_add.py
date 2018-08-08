# encoding: utf-8
"""对直接创建的质检工单报检"""

import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.报检单 import QualityRecord
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params


class QualityRecordAdd(unittest.TestCase):
    """报检单"""

    def setUp(self):
        self.qr = QualityRecord()
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

        self.qualityRecord_data = {
            "code":"",
            "qcInspectionQty": 5,
            "imeQcQacGid":resp1.pop("data")
        }
        # 质检工单生成报检单的入参


    def test_qualityRecordAdd(self):
        """对直接创建的质检工单报检"""

        resp2 = self.qr.qualityRecord_add(self.qualityRecord_data)
        print(resp2)
        self.assertEqual(True,resp2.pop("success"))
        """质检工单生成报检单"""

        self.reportRecord_data = {
        "qualifiedQty":1,
        "unQualifiedQty":1,
        "imeQcQualityGradeGid":"",
        "qcHandleWay":"",
        "gid":resp2.pop("data")
        }
        # 报检单报检的入参

        resp3 = self.qr.reportRecord(self.reportRecord_data)
        print(resp3)
        self.assertEqual(True, resp3.pop("success"))
        """报检单报检"""


if __name__ == '__main__':
    unittest.main()