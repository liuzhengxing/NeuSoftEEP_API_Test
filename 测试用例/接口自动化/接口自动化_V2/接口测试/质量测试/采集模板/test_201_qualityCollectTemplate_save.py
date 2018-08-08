#encoding = 'utf-8'
"""采集模板创建与保存"""
import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质量采集模板 import QualityCollectTemplate
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params

class QualityCollectTemplateSave(unittest.TestCase):
    """采集模板创建"""

    def setUp(self):
        self.qct = QualityCollectTemplate()
        self.QualityCollectTemplate_data = {
            "code":pm.create_code(),
            "name":"模板Aug",
            "materialGid":params.MaterielSJGid,
            "bmOperationGid":params.bmOperationInfoCPUGid,
            "bmOperationCode":"001",
            "bmOperationName":"CPU工序"
        }


    def test_qualityWorkOrderRef(self):


        status = self.qct.saveQualityCollectTemplate(self.QualityCollectTemplate_data)
        """采集模板创建与保存"""

        print(status)
        self.assertEqual(True,status.pop('success'))


if __name__ == '__main__':
    unittest.main()