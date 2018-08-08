# encoding: utf-8

import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质量采集清单 import QualityCollectList
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from public import params


class TestQualityCollectListAddBatch(unittest.TestCase):
    """采集清单批量创建测试类"""

    def setUp(self):
        self.qcl = QualityCollectList()

        self.qwo = QualityWorkOrder()

        self.qualityWorkOrder_data = {
            "smBusiUnitGid": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
            "code": "",
            "mdMaterialGid": params.MaterielSJGid,
            "shouldCheckQty": 10
        }

        self.qualityCollectList_data = [
            {
                "importance": "important",
                "indexCode": "001",
                "indexCreateSourceGid": "60eca75873644e91b09b082d963bf76e",
                "indexName": "轴承",
                "indexType": "qualitative",
                "mdRouteOperationCode": "001",
                "mdRouteOperationName": "冲压工序01",
                "isOk": "b40fde533e474fdb97f0e51d4439fa2a",
                "qcRefCode": "",
                "qcRefGid": "",
                "qcRefType": ""
            }
        ]

    def test_cl_createBy_qwo(self):
        """根据质检工单创建采集清单"""

        # 直接创建一条质检工单
        qwoCode = 'QWO' + pm.create_code()
        self.qualityWorkOrder_data['code'] = qwoCode
        resp_qwo_create = self.qwo.qualityWorkOrder_create(self.qualityWorkOrder_data)

        qwoGid = resp_qwo_create.get('data')

        self.qualityCollectList_data[0]['qcRefGid'] = qwoGid
        self.qualityCollectList_data[0]['qcRefType'] = "20010"
        resp_qcl_addBatch = self.qcl.qualityCollectList_addBatch(self.qualityCollectList_data)

        self.assertLess(0, len(resp_qcl_addBatch.get('data')))


if __name__ == '__main__':
    unittest.main()
