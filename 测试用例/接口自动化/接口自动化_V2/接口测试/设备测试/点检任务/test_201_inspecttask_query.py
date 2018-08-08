# _*_ coding:utf-8 _*

import unittest

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检任务 import InspectTask


class TestInspectTaskQuery(unittest.TestCase):
    """点检任务列表查询测试类"""

    def setUp(self):
        self.it = InspectTask()

        self.it_query_data = {
            "query": {
                "query": [
                    {
                        "field": "bmEquipmentGid",
                        "type": "eq",
                        "value": params.bmEquipmentGid,
                        "operator": "and"
                    }
                ]
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

    def test_inspecttask_query_1(self):
        """
        点检任务列表查询
        :return:
        """
        self.it.inspecttask_query = Mock(side_effect=self.it.inspecttask_query)
        resp_it_query = self.it.inspecttask_query(self.it_query_data)

        self.assertLess(0, len(resp_it_query.get('data')))


if __name__ == "__main__":
    unittest.main()
