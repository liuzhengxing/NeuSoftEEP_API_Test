# _*_coding: utf-8 _*_

import unittest
import requests
import json

from public import params
from public import excel

domain = params.testdomain
port = params.testport


class InspectPlanCreate(unittest.TestCase):
    u'''点检计划创建'''
    def setUp(self):
        pass

    def test_inspectplan_create_year(self):
        u'''按年单位创建点检计划'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/save.action'
        headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }
        data = {
            'smDepartmentGid': excel.excel_find('DepartmentGid'),
            'smDepartmentName': '自动化测试',
            'startDate': '2017-11-29',
            'endDate': '2018-01-03',
            'imeInspectPlanInfoDetailList':
                [{
                    'mdInspectObjectGid': excel.excel_find('EquipInspectItemGid'),
                    'mdInspectObjectGidRef': {'itemName': 'round1'},
                    'inspectCycle': '1',
                    'unit': '年',
                    'generatedCycle': '年',
                    'inspectMode': 'sight',
                    'inspectStandard': '点检标准'
                }]
        }
        req = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
        # print(req)
        if '"data":"' in req and '"success":true' in req:
            assert 1 == 1
        else:
            assert 1 == 2


    def test_inspectplan_create_month(self):
        u'''按月单位创建点检计划'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/save.action'
        headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }
        data = {
            'smDepartmentGid': excel.excel_find('DepartmentGid'),
            'smDepartmentName': '自动化测试',
            'startDate': '2017-11-29',
            'endDate': '2018-01-03',
            'imeInspectPlanInfoDetailList':
                [{
                    'mdInspectObjectGid': excel.excel_find('EquipInspectItemGid'),
                    'mdInspectObjectGidRef': {'itemName': 'round1'},
                    'inspectCycle': '1',
                    'unit': '月',
                    'generatedCycle': '年',
                    'inspectMode': 'sight',
                    'inspectStandard': '点检标准'
                }]
        }
        req = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
        # print(req)
        if '"data":"' in req and '"success":true' in req:
            assert 1 == 1
        else:
            assert 1 == 2


    def test_inspectplan_create_day(self):
        u'''按天单位创建点检计划'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/save.action'
        headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }
        data = {
            'smDepartmentGid': excel.excel_find('DepartmentGid'),
            'smDepartmentName': '自动化测试',
            'startDate': '2017-11-29',
            'endDate': '2018-01-03',
            'imeInspectPlanInfoDetailList':
                [{
                    'mdInspectObjectGid': excel.excel_find('EquipInspectItemGid'),
                    'mdInspectObjectGidRef': {'itemName': 'round1'},
                    'inspectCycle': '1',
                    'unit': '天',
                    'generatedCycle': '月',
                    'inspectMode': 'sight',
                    'inspectStandard': '点检标准'
                }]
        }
        req = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
        # print(req)
        if '"data":"' in req and '"success":true' in req:
            assert 1 == 1
        else:
            assert 1 == 2


    def test_inspectplan_create_hour(self):
        u'''按时单位创建点检计划'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/save.action'
        headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }
        data = {
            'smDepartmentGid': excel.excel_find('DepartmentGid'),
            'smDepartmentName': '自动化测试',
            'startDate': '2017-11-29',
            'endDate': '2018-01-03',
            'imeInspectPlanInfoDetailList':
                [{
                    'mdInspectObjectGid': excel.excel_find('EquipInspectItemGid'),
                    'mdInspectObjectGidRef': {'itemName': 'round1'},
                    'inspectCycle': '5',
                    'unit': '时',
                    'generatedCycle': '天',
                    'inspectMode': 'sight',
                    'inspectStandard': '点检标准'
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
