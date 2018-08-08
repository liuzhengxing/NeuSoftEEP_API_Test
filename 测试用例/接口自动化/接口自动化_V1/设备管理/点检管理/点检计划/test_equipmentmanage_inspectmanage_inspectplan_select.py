# _*_coding: utf-8 _*_

import unittest

import requests

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import inspectplan_public

domain = params.testdomain
port = params.testport
headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }


class InspectPlanDetailSelect(unittest.TestCase):
    u'''点检计划查询'''
    def setUp(self):
        pass

    def test_inspectplan_detailselect(self):
        u'''查询点检计划详情'''
        # 创建点检计划
        ipgid = inspectplan_public.inspectplan_create()
        # print('============', gid)
        # 按gid查询点检计划详情
        req = inspectplan_public.inspectplan_select(ipgid)
        print(req)
        if ipgid in req:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_inspectplan_listselect_all(self):
        u'''列表查询点检计划'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/query.action'
        req = requests.get(interfaceurl, headers=headers).content.decode()
        # print(req)
        if '"data":' in req and '"success":true' in req and '"pager":' in req:
            assert 1 == 1
        else:
            assert 1 == 2

    # def test_inspectplan_listselect_(self):
    #     u'''列表查询点检计划'''
    #     interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/query.action'
    #     data = {
    #         "query":
    #             {"query": [{
    #                      "left": "(", "field": "code", "type": "like", "value": "20180226",
    #                      "operator": "or", "right": ")"}]
    #              },
    #         "pager": {"page": 1, "pageSize": 10}}
    #     req = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    #     # print(req)
    #     if '"data":' in req and '"success":true' in req and '"pager":' in req:
    #         assert 1 == 1
    #     else:
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main(0)
