# _*_coding:utf-8_*_

import requests
import json

from public import params
from public import excel

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def overhaulplan_create():
    u'''创建大修计划'''
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
    return opgid


def overhaulplan_select(opgid):
    u'''查询大修计划详情'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulPlan/findById.action?gid=' + opgid
    opsreq = requests.get(interfaceurl, headers=headers).content.decode()
    return opsreq


# def iverhaulplan_find(opgode):
#     u'''按大修计划编号查询'''
#     interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulPlan/query.action?usedPost=true '
#     fdata = {
#         "query":{
#             "query":[
#                 {"left":"(","field":"code","type":"like","value":opgode,"operator":"or"},
#                 {"field":"type","type":"like","value":opgode,"operator":"or"},
#                 {"field":"smDepartmentName","type":"like","value":opgode,"operator":"or"},
#                 {"field":"startDate","type":"like","value":opgode,"operator":"or"},
#                 {"field":"endDate","type":"like","value":opgode,"operator":"or"},
#                 {"right":")","field":"status","type":"like","value":opgode,"operator":"and"}
#             ]
#         },
#         "pager":{"page":1,"pageSize":10}
#     }
#     opfreq = requests.post(interfaceurl, headers=headers, data=json.dumps(fdata)).content.decode()
#     return opfreq


def overhaulplan_delete(opgids):
    u'''查询大修计划详情'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulPlan/delete.action'
    opdreq = requests.post(interfaceurl, headers=headers, data=json.dumps(opgids)).content.decode()
    return opdreq


def overhaulplan_senddown(opgids):
    u'''发布大修计划'''
    interfaceurl= 'http://' + domain + ':' + port + '/ime-container/imeOverhaulPlan/publish.action'
    opsdreq = requests.post(interfaceurl, headers=headers, data=json.dumps(opgids)).content.decode()
    return opsdreq
