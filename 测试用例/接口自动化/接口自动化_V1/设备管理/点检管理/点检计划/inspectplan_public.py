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


def inspectplan_create():
    u'''创建点检计划'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/save.action'
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
    gid = json.loads(req)['data']
    return gid


def inspectplan_select(ipgid):
    u'''查询点检计划详情'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/findById.action?gid=' + ipgid
    sreq = requests.get(interfaceurl, headers=headers).content.decode()
    return sreq


def inspectplan_delete(ipgids):
    u'''删除点检计划'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/delete.action'
    dreq = requests.post(interfaceurl, headers=headers, data=json.dumps(ipgids)).content.decode()
    return dreq


def inspectplan_senddown(ipgids):
    u'''发布点检计划'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectPlan/publish.action'
    sdreq = requests.post(interfaceurl, headers=headers, data=json.dumps(ipgids)).content.decode()
    return sdreq