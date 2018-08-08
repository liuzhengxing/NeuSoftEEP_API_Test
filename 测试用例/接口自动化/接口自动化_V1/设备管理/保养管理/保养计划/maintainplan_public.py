# _*_coding: utf-8 _*_

import requests
import json

from public import params
from public import excel

domain = params.testdomain
port = params.testport

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def maintainplan_create():
    '''创建保养计划'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainPlan/planSave.action'
    data = {
        "smDepartmentGid": excel.excel_find('DepartmentGid'),
        "smDepartmentName": "接口自动化_V1",
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
    gid = json.loads(req)['data']
    return gid


def maintainplan_select(mgid):
    '''查询保养计划详情'''
    selecturl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainPlan/findById.action?gid=' + mgid
    sreq = requests.get(selecturl, headers=headers).content.decode()
    return sreq


def maintainplan_delete(mgids):
    '''删除保养计划'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainPlan/delete.action'
    dreq = requests.post(interfaceurl, headers=headers, data=json.dumps(mgids)).content.decode()
    return dreq


def maintainplan_senddown(mgids):
    '''下发保养计划'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainPlan/publish.action'
    dreq = requests.post(interfaceurl, headers=headers, data=json.dumps(mgids)).content.decode()
    return dreq