# _*_coding:utf-8_*_

import json
import unittest

import requests

from public import excel
from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class OverhaulPlanCreate(unittest.TestCase):
    u'''大修单创建'''
    def setUp(self):
        pass

    def test_overhaulplan_create_year(self):
        u'''按年单位创建大修单'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulPlan/planSave.action'
        cdata = {
            "smDepartmentGid": excel.excel_find('DepartmentGid'),
            "smDepartmentName": "自动化测试",
            "startDate": "2017-12-30",
            "endDate": "2018-02-03",
            "type": "year_check",
            "imeOverhaulPlanInfoList": [{
                "eventPayload": {},
                "content": "大修内容",
                "cycle": "1",
                "cycleUnit": "year",
                "standard": "大修标准"
            }]
        }
        opcreq = requests.post(interfaceurl, headers=headers, data=json.dumps(cdata)).content.decode()
        opgid = json.loads(opcreq)['data']
        sreq = overhaulplan_public.overhaulplan_select(opgid)
        if opgid in sreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_overhaulplan_create_month(self):
        u'''按月单位创建大修单'''
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulPlan/planSave.action'
        cdata = {
            "smDepartmentGid": excel.excel_find('DepartmentGid'),
            "smDepartmentName": "自动化测试",
            "startDate": "2017-12-30",
            "endDate": "2018-02-03",
            "type": "year_check",
            "imeOverhaulPlanInfoList": [{
                "eventPayload": {},
                "content": "大修内容",
                "cycle": "1",
                "cycleUnit": "month",
                "standard": "大修标准"
            }]
        }
        opcreq = requests.post(interfaceurl, headers=headers, data=json.dumps(cdata)).content.decode()
        opgid = json.loads(opcreq)['data']
        sreq = overhaulplan_public.overhaulplan_select(opgid)
        if opgid in sreq:
            assert 1 == 1
        else:
            assert 1 == 2