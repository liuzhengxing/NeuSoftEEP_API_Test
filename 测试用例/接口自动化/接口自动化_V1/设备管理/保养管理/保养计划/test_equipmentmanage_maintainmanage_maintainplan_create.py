# _*_coding: utf-8 _*_

import unittest
import requests
import json

from public import params
from public import excel

domain = params.testdomain
port = params.testport
headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }
interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainPlan/planSave.action'


class MaintainPlanCreate(unittest.TestCase):
    u'''保养计划创建'''
    def setUp(self):
        pass

    def test_maintainplan_create_year(self):
        u'''按年单位创建保养计划'''
        data = {
            "smDepartmentGid": excel.excel_find('DepartmentGid'),
            "smDepartmentName": "保时捷部门",
            "startDate": "2017-11-29",
            "endDate": "2018-01-03",
            "type": "daily_maintain",
            "imeMaintainPlanInfoList": [{
                "eventPayload": {},
                "content": "保养内容",
                "cycle": "1",
                "cycleUnit": "year",
                "standard": "保养标准"
            }]
        }
        req = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
        # print(req)
        if '"data":"' in req and '"success":true' in req:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_maintainplan_create_month(self):
        u'''按月单位创建保养计划'''
        data = {
            "smDepartmentGid": excel.excel_find('DepartmentGid'),
            "smDepartmentName": "保时捷部门",
            "startDate": "2017-11-29",
            "endDate": "2018-01-03",
            "type": "daily_maintain",
            "imeMaintainPlanInfoList": [{
                "eventPayload": {},
                "content": "保养内容",
                "cycle": "1",
                "cycleUnit": "month",
                "standard": "保养标准"
            }]
        }
        req = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
        # print(req)
        if '"data":"' in req and '"success":true' in req:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_maintainplan_create_day(self):
        u'''按天单位创建保养计划'''
        data = {
            "smDepartmentGid": excel.excel_find('DepartmentGid'),
            "smDepartmentName": "保时捷部门",
            "startDate": "2017-11-29",
            "endDate": "2018-01-03",
            "type": "daily_maintain",
            "imeMaintainPlanInfoList": [{
                "eventPayload": {},
                "content": "保养内容",
                "cycle": "1",
                "cycleUnit": "day",
                "standard": "保养标准"
            }]
        }
        req = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
        # print(req)
        if '"data":"' in req and '"success":true' in req:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main(0)
