#encoding = 'utf-8'
"""删除指标值"""
import unittest

from unittest.mock import Mock
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质量采集模板 import QualityCollectTemplate
from 测试用例.接口自动化.接口自动化_V2.接口测试 import public_method as pm
from public import params

class QualityIndexValueSave(unittest.TestCase):
    """指标创建"""

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
        """首先，创建模板"""

        self.qualityIndexType_data = [{
            "code": pm.create_code(),
            "name": "分类Aug",
            "childrenList":
                {
                    "code": pm.create_code(),
                    "name": "分类Aug-1"
                }
        }]
        """其次，创建指标分类"""


    def test_qualityWorkOrderRef(self):

        resp1 = self.qct.saveQualityCollectTemplate(self.QualityCollectTemplate_data)
        """创建模板"""

        self.qct.saveIndexType(self.qualityIndexType_data, resp1["data"])
        """指标分类创建"""

        resp2 = self.qct.queryIndexTypeTree(resp1["data"])
        """根据指标分类模糊查询末级指标分类GID"""

        self.QualityIndexValue_data = [{
            "code": pm.create_code(),
            "name": "指标Aug",
            "descritption": "TestDesc",
            "value": "TestValue",
            "indexTypeGid":resp2["data"][0]["childrenList"][0]["gid"] ,
            "optionsType": "characterType",
            "indexOptionsList": [{
                "code": pm.create_code(),
                "name": "选项01"
            },
                {
                    "code": pm.create_code(),
                    "name": "选项02"
                }
            ]
        }]

        resp3 = self.qct.saveIndexValue(self.QualityIndexValue_data)
        """保存指标值，同时保存选项"""


        resp4 = self.qct.deleteIndexValue(resp3["data"])
        self.assertEqual(True,resp4["success"])
        """删除指标值"""

if __name__ == '__main__':
    unittest.main()