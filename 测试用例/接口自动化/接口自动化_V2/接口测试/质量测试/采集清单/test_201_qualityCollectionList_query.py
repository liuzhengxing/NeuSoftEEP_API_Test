# encoding = utf-8

import unittest

from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质量采集清单 import QualityCollectList
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.派检单 import TrackQualityOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.报检单 import QualityRecord

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm


class TestQualityCollectionListQuery(unittest.TestCase):

    def setUp(self):
        self.qc = QualityCollectList()
        self.qwo = QualityWorkOrder()
        self.tqo = TrackQualityOrder()
        self.qro = QualityRecord()

        self.qualityWorkOrder_data_create = {
            "smBusiUnitGid": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
            "code": "",
            "mdMaterialGid": params.MaterielSJGid,
            "shouldCheckQty": 10
        }

        self.tqo_data_create = {
            "code": "",
            "qcDispatchedQty": 10,
            "mdFactoryWorkStationGid": params.bmFactoryWorkStationCPUGid,
            "imeQcQualityWayGid": "",
            "surveyor": "",
            "checkBeginTime": "",
            "checkEndTime": "",
            "remarks": "",
            "imeQcQacGid": "",
            "imeQcQacCode": "",
            "mdMaterialGid": "",
            "mdProductInfoGid": "",
            "qcHasDispatchedQty": "",
            "qcHasInspectionQty": "",
            "qcDispatchedPersonGid": ""
        }

        self.rqo_data_create = {
            "code": "",
            "qcInspectionQty": 10,
            "imeQcQacBillGid": ""
        }

    def test_qualityCollectionList_queryBy_QWO(self):
        """根据质检工单查询检测指标"""

        # 创建质检工单
        QWO_code = 'QWO' + pm.create_code()
        self.qualityWorkOrder_data_create['code'] = QWO_code
        resp_QWO_create = self.qwo.qualityWorkOrder_create(self.qualityWorkOrder_data_create)
        QWOGid = resp_QWO_create.get('data')

        resp_qcl_query = self.qc.qualityCollectList_query(QWOGid, 20010)
        self.assertEqual(True, resp_qcl_query.pop("success"))

    def test_qualityCollectionList_queryBy_TQO(self):
        """根据派检单查询检测指标"""

        # 创建质检工单
        QWO_code = 'QWO' + pm.create_code()
        self.qualityWorkOrder_data_create['code'] = QWO_code
        resp_QWO_create = self.qwo.qualityWorkOrder_create(self.qualityWorkOrder_data_create)
        QWOGid = resp_QWO_create.get('data')

        # 生成派检单
        self.tqo_data_create['imeQcQacGid'] = QWOGid
        self.tqo_data_create['imeQcQacCode'] = QWO_code
        resp_TQO_create = self.tqo.trackQualityOrder_add(self.tqo_data_create)
        tqoGid = resp_TQO_create.get('data')

        resp_qcl_query = self.qc.qualityCollectList_query(tqoGid, 20011)
        self.assertEqual(True, resp_qcl_query.pop("success"))

    def test_qualityCollectionList_queryBy_RQO(self):
        """根据报检单查询检测指标"""

        # 创建质检工单
        QWO_code = 'QWO' + pm.create_code()
        self.qualityWorkOrder_data_create['code'] = QWO_code
        resp_QWO_create = self.qwo.qualityWorkOrder_create(self.qualityWorkOrder_data_create)
        QWOGid = resp_QWO_create.get('data')

        # 生成派检单
        self.tqo_data_create['imeQcQacGid'] = QWOGid
        self.tqo_data_create['imeQcQacCode'] = QWO_code
        resp_TQO_create = self.tqo.trackQualityOrder_add(self.tqo_data_create)
        tqoGid = resp_TQO_create.get('data')

        # 生成报检单
        self.rqo_data_create['imeQcQacBillGid'] = tqoGid
        resp_rqo_create = self.qro.qualityRecord_add(self.rqo_data_create)

        # 报检单GID
        rqoGid = resp_rqo_create.get('data')

        resp_qcl_query = self.qc.qualityCollectList_query(rqoGid, 20012)
        self.assertEqual(True, resp_qcl_query.pop("success"))


if __name__ == "__main__":
    unittest.main()