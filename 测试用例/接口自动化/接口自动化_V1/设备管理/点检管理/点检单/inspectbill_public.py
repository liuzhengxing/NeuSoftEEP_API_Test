# _*_coding:utf-8_*_

import json

import requests

from public import excel
from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import equipmentmanage_public
from 测试用例.接口自动化.接口自动化_V1.设备管理 import inspectplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def inspectbill_select(ibgid):
    u'''查询点检单详情'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectBill/findById.action?gid=' + ibgid
    sreq = requests.get(interfaceurl, headers=headers).content.decode()
    return sreq


def inspectbill_find(ipcode):
    u'''根据点检计划编号查询点检单'''
    searchurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectBill/query.action?usedPost=true'
    data = {"query":
                {"query":[
                    {"left":"(","field":"code","type":"like","value":ipcode,"operator":"or"},
                    {"field":"imeInspectPlanCode","type":"like","value":ipcode,"operator":"or"},
                    {"field":"mdEquipmentGidRef.code","type":"like","value":ipcode,"operator":"or"},
                    {"field":"mdEquipmentGidRef.name","type":"like","value":ipcode,"operator":"or"},
                    {"field":"mdEquipmentGidRef.spec","type":"like","value":ipcode,"operator":"or"},
                    {"field":"mdEquipmentGidRef.model","type":"like","value":ipcode,"operator":"or"},
                    {"field":"inspectCycle","type":"like","value":ipcode,"operator":"or"},
                    {"field":"unit","type":"like","value":ipcode,"operator":"or"},
                    {"field":"generatedCycle","type":"like","value":ipcode,"operator":"or"},
                    {"field":"smPersonnelGidRef.personnelName","type":"like","value":ipcode,"operator":"or"},
                    {"right":")","field":"status","type":"like","value":ipcode,"operator":"and"}]},
        "pager":{"page":1,"pageSize":10}
    }
    freq = requests.get(searchurl, headers=headers, data=json.dumps(data)).content.decode()
    return freq


def inspectbill_create():
    u'''创建点检单'''
    # 创建点检计划
    ipgids = []
    ipgid = inspectplan_public.inspectplan_create()
    ipgids.append(ipgid)

    # 查询点检计划编号
    sreq = inspectplan_public.inspectplan_select(ipgid)
    ipcode = json.loads(sreq)['data']['code']

    # 关联设备
    equipmentmanage_public.associationequipment(ipgid)

    # 发布
    inspectplan_public.inspectplan_senddown(ipgids)

    # 按保养计划编号查询保养单gid
    sreq = inspectbill_find(ipcode)
    ibgid = json.loads(sreq)['data'][0]['gid']
    return ibgid


def inspectbill_findCrosswiseById(ibgid):
    u'''查询点检单详情子表信息'''
    interfaceurl = 'http://' + domain + ':' + port + \
                   '/ime-container/imeInspectBill/findCrosswiseById.action?gid=' + ibgid
    freq = requests.get(interfaceurl, headers=headers).content.decode()
    return freq


def inspectbill_dispatch(mbgids):
    u'''点检单派工'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectBill/trackInspectBill.action'
    data = {"gids": mbgids, "smPersonnelGid": excel.excel_find('PersonnelGid')}
    bdreq = requests.get(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return bdreq


def inspectbill_report():
    u'''点检单报工'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectBill/report.action'


def inspectbill_modify():
    u'''点检单修改'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeInspectBill/modifyByCrosswise.action'