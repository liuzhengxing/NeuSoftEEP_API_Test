# encoding: utf-8
"""对直接创建的质检工单先派检，再报检"""

import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.派检单 import TrackQualityOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.报检单 import QualityRecord
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params


class QualityRecord_TrackAdd(unittest.TestCase):
    """派检单"""

    def setUp(self):
        self.qwo = QualityWorkOrder()
        self.tqo = TrackQualityOrder()
        self.qr = QualityRecord()

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
            "qcDispatchedQty": 5,
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

        resp2 = self.tqo.trackQualityOrder_add(self.trackQualityOrder_data)
        print("resp2")
        print(resp2)
        # 对质检工单做派检

        self.qualityRecord_data = {
            "code": "",
            "qcInspectionQty": 2,
            "imeQcQacBillGid": resp2.pop("data")
        }

        resp3 = self.qr.qualityRecord_add(self.qualityRecord_data)
        print("resp3")
        print(resp3)
        # 根据派检单生成报检单

        self.reportRecord_data = {
            "qualifiedQty": 1,
            "unQualifiedQty": 1,
            "imeQcQualityGradeGid": "",
            "qcHandleWay": "返工返修",
            "gid": resp3.pop("data")
        }
        # 报检单报检的入参



    def test_trackQualityOrder(self):
        """报检"""

        resp4 = self.qr.reportRecord(self.reportRecord_data)
        print("resp4")
        print(resp4)
        self.assertEqual(True,resp4.pop("success"))


if __name__ == '__main__':
    unittest.main()