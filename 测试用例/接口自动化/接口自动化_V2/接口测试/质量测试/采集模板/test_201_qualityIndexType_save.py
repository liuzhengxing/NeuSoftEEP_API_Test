#encoding = 'utf-8'
"""保存分类，用于新增和修改，并关联模板"""
import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质量采集模板 import QualityCollectTemplate
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params

class QualityIndexTypeSave(unittest.TestCase):
    """指标分类创建"""

    def setUp(self):
        self.qct = QualityCollectTemplate()

        self.QualityCollectTemplate_data = {
            "code": pm.create_code(),
            "name": "模板Aug",
            "materialGid": params.MaterielSJGid,
            "bmOperationGid": params.bmOperationInfoCPUGid,
            "bmOperationCode": "001",
            "bmOperationName": "CPU工序"
        }

        self.qualityIndexType_data =  [{
            "code":pm.create_code(),
            "name":"分类Aug",
            "childrenList":
            {
            "code":pm.create_code(),
            "name":"分类Aug-1"
            }
        }]

    def test_qualityWorkOrderRef(self):
        resp = self.qct.saveQualityCollectTemplate(self.QualityCollectTemplate_data)
        """创建模板"""

        # print(resp)

        status = self.qct.saveIndexType(self.qualityIndexType_data,resp["data"])
        """指标分类创建与保存"""

        # print(status)
        self.assertEqual(True,status.pop('success'))


if __name__ == '__main__':
    unittest.main()