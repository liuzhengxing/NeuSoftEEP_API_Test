# _*_coding: utf-8 _*_

import json

import requests

from public import excel
from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import equipmentmanage_public
from 测试用例.接口自动化.接口自动化_V1.设备管理 import maintainplan_public

domain = params.testdomain
port = params.testport

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def maintainbill_select(mgid):
    '''查询保养单详情'''
    selecturl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainBill/findById.action?gid=' + mgid
    sreq = requests.get(selecturl, headers=headers).content.decode()
    return sreq

def maintainbill_create():
    u'''生成保养单'''
    # 创建保养计划
    mpgids = []
    mpgid = maintainplan_public.maintainplan_create()
    # print(mgid)
    mpgids.append(mpgid)
    # 获取保养计划编号
    sreq = maintainplan_public.maintainplan_select(mpgid)
    code = json.loads(sreq)['data']['code']
    # print('======', code)
    # 关联设备
    equipmentmanage_public.associationequipment(mpgid)
    # 发布保养单
    maintainplan_public.maintainplan_senddown(mpgids)
    # 按保养计划编号查询保养单
    searchurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainBill/query.action?usedPost=true'
    data = {
        "query": {"query": [{"left": "(", "field": "mdEquipmentName", "type": "like", "value": code, "operator": "or"},
                            {"field": "imeMaintainPlanCode", "type": "like", "value": code, "operator": "or"},
                            {"right": ")", "field": "code", "type": "like", "value": code, "operator": "and"}]},
        "pager": {"page": 1, "pageSize": 10}
    }
    sreq = requests.post(searchurl, headers=headers, data=json.dumps(data)).content.decode()
    # 获取第一个保养单gid
    mbgid = json.loads(sreq)['data'][0]['gid']
    return mbgid

def maintainbill_dispatch(mbgids):
    u'''保养单派工'''
    dpurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainBill/billDispatch.action'
    data = {"gids": mbgids,
            "imeMaintainBill": {
                "smPersonnelGid": excel.excel_find('PersonnelGid'),
                "smPersonnelName": "接口自动化测试人员"
            }
    }
    dpreq = requests.post(dpurl, headers=headers, data=json.dumps(data)).content.decode()
    return dpreq

def maintainbill_saveorrecord(mbgid, action):
    u'''保养单保存或报工'''
    sreq = maintainbill_select(mbgid)
    sdjson = json.loads(sreq)['data']
    # 参数值
    mdEquipmentName = sdjson['mdEquipmentName']
    imeMaintainPlanCode = sdjson['imeMaintainPlanCode']
    gid = sdjson['gid']
    mdEquipmentCode = sdjson['mdEquipmentCode']
    cycle = sdjson['cycle']
    cycleUnit = sdjson['cycleUnit']
    mdEquipmentGid = sdjson['mdEquipmentGid']
    imeMaintainPlanGid = sdjson['imeMaintainPlanGid']
    code = sdjson['code']
    imeMaintainPlanType = sdjson['imeMaintainPlanType']
    startDate = sdjson['startDate']
    smPersonnelName = sdjson['smPersonnelName']
    mdEquipmentSpec = sdjson['mdEquipmentSpec']
    mdEquipmentModel = sdjson['mdEquipmentModel']
    status = sdjson['status']
    smPersonnelGid = sdjson['smPersonnelGid']
    standard = sdjson['imeMaintainBillInfoList'][0]['standard']
    gid2 = sdjson['imeMaintainBillInfoList'][0]['gid']
    imeMaintainPlanInfoGid = sdjson['imeMaintainBillInfoList'][0]['imeMaintainPlanInfoGid']
    content = sdjson['imeMaintainBillInfoList'][0]['content']
    data = {
        "mdEquipmentName": mdEquipmentName,
        "imeMaintainPlanCode": imeMaintainPlanCode,
        "imeMaintainBillSpareList": [],
        "gid": gid,
        "mdEquipmentCode": mdEquipmentCode,
        "cycle": cycle,
        "cycleUnit": cycleUnit,
        "mdEquipmentGid": mdEquipmentGid,
        "imeMaintainPlanGid": imeMaintainPlanGid,
        "code": code,
        "imeMaintainPlanType": imeMaintainPlanType,
        "startDate": startDate,
        "smPersonnelName": smPersonnelName,
        "mdEquipmentSpec": mdEquipmentSpec,
        "mdEquipmentModel": mdEquipmentModel,
        "status": status,
        "smPersonnelGid": smPersonnelGid,
        "imeMaintainBillInfoList":
            [{"standard": standard,
              "gid": gid2,
              "imeMaintainPlanInfoGid": imeMaintainPlanInfoGid,
              "content": content,
              "result": "保养结果"
              }]
    }
    dpurl = ''
    if action == 'record':
        dpurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainBill/billRecord.action'
    elif action == 'save':
        dpurl = 'http://' + domain + ':' + port + '/ime-container/imeMaintainBill/billSave.action'
    brreq = requests.post(dpurl, headers=headers, data=json.dumps(data)).content.decode()
    return brreq