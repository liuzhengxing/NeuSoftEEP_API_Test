#encoding = 'utf-8'
"""对直接创建的质检工单派检"""
import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.派检单 import TrackQualityOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params


class TrackQualityOrderAdd(unittest.TestCase):
    """派检单"""

    def setUp(self):
        self.qwo = QualityWorkOrder()
        self.tqo = TrackQualityOrder()

        self.qualityWorkOrder_data = {
            "smBusiUnitGid": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
            "code": pm.create_code(),
            "mdMaterialGid": params.MaterielSJGid,
            "shouldCheckQty": 10
        }

        resp1 = self.qwo.qualityWorkOrder_create(self.qualityWorkOrder_data)
        # print(resp1)
        # 直接创建一条质检工单

        self.trackQualityOrder_data = {
            "code": pm.create_code(),
            "qcDispatchedQty": 1,
            "mdFactoryWorkStationGid": "",
            "imeQcQualityWayGid": "",
            "surveyor": "",
            "checkBeginTime": "",
            "checkEndTime": "",
            "remarks": "",
            "imeQcQacGid": resp1.pop("data"),
            "imeQcQacCode": "",
            "mdMaterialGid": "",
            "mdProductInfoGid": "",
            "qcHasDispatchedQty": "",
            "qcHasInspectionQty": "",
            "qcDispatchedPersonGid": ""
        }

    def test_trackQualityOrder(self):
        """对直接创建的质检工单派检"""

        resp2 = self.tqo.trackQualityOrder_add(self.trackQualityOrder_data)
        print(resp2)
        self.assertEqual(True,resp2.pop("success"))


if __name__ == '__main__':
    unittest.main()