# _*_coding:utf-8_*_

import json

import requests

from public import excel
from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import equipmentmanage_public
from 测试用例.接口自动化.接口自动化_V1.设备管理 import overhaulplan_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def overhaulbill_create():
    u'''生成大修单'''
    opgids = []
    opgid = overhaulplan_public.overhaulplan_create()
    opgids.append(opgid)
    opsreq = overhaulplan_public.overhaulplan_select(opgid)
    opcode = json.loads(opsreq)['data']['code']
    equipmentmanage_public.associationequipment(opgid)
    overhaulplan_public.overhaulplan_senddown(opgids)
    obfreq = overhaulbill_findbycode(opcode)
    obgid = json.loads(obfreq)['data'][0]['gid']
    return obgid


def overhaulbill_select(obgid):
    u'''查询大修单详情'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulBill/findById.action?gid=' + obgid
    obsreq = requests.get(interfaceurl, headers=headers).content.decode()
    return obsreq


def overhaulbill_findbycode(opcode):
    u'''按大修计划编号查询大修单'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulBill/query.action?usedPost=true'
    data = {
        "query":{
            "query":[
                {"left":"(","field":"code","type":"like","value":opcode,"operator":"or"},
                {"field":"imeOverhaulPlanCode","type":"like","value":opcode,"operator":"or"},
                {"field":"mdEquipmentCode","type":"like","value":opcode,"operator":"or"},
                {"field":"mdEquipmentName","type":"like","value":opcode,"operator":"or"},
                {"field":"imeOverhaulPlanType","type":"like","value":opcode,"operator":"or"},
                {"field":"mdEquipmentSpec","type":"like","value":opcode,"operator":"or"},
                {"field":"mdEquipmentModel","type":"like","value":opcode,"operator":"or"},
                {"field":"cycle","type":"like","value":opcode,"operator":"or"},
                {"field":"cycleUnit","type":"like","value":opcode,"operator":"or"},
                {"field":"smPersonnelName","type":"like","value":opcode,"operator":"or"},
                {"right":")","field":"status","type":"like","value":opcode,"operator":"and"}]},
        "pager":{"page":1,"pageSize":10}
    }
    obfreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return obfreq


def overhaulbill_dispatch(obgids):
    u'''大修单派工'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulBill/billDispatch.action'
    data = {
        "gids": obgids,
        "imeOverhaulBill": {"smPersonnelGid": excel.excel_find('PersonnelGid'), "smPersonnelName": "接口自动化测试人员"}
    }
    obdpreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return obdpreq


def overhaulbill_saveorrecord(obgid, action):
    u'''大修单报工'''
    obsreq = overhaulbill_select(obgid)
    obsjson = json.loads(obsreq)['data']
    mdEquipmentName = obsjson['mdEquipmentName']
    gid = obsjson['gid']
    mdEquipmentCode = obsjson['mdEquipmentCode']
    cycle = obsjson['cycle']
    imeOverhaulPlanType = obsjson['imeOverhaulPlanType']
    endDate = obsjson['endDate']
    cycleUnit = obsjson['cycleUnit']
    mdEquipmentGid = obsjson['mdEquipmentGid']
    code = obsjson['code']
    startDate = obsjson['startDate']
    smPersonnelName = obsjson['smPersonnelName']
    # mdEquipmentSpec = obsjson['mdEquipmentSpec']
    mdEquipmentModel = obsjson['mdEquipmentModel']
    status = obsjson['status']
    imeOverhaulPlanGid = obsjson['imeOverhaulPlanGid']
    standard = obsjson['imeOverhaulBillInfoList'][0]['standard']
    obilgid = obsjson['imeOverhaulBillInfoList'][0]['gid']
    imeOverhaulBillGid = obsjson['imeOverhaulBillInfoList'][0]['imeOverhaulBillGid']
    imeOverhaulPlanInfoGid = obsjson['imeOverhaulBillInfoList'][0]['imeOverhaulPlanInfoGid']
    content = obsjson['imeOverhaulBillInfoList'][0]['content']
    imeOverhaulPlanCode = obsjson['imeOverhaulPlanCode']
    smPersonnelGid = obsjson['smPersonnelGid']
    interfaceurl = ''
    if action == 'record':
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulBill/billRecord.action'
    elif action == 'save':
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeOverhaulBill/billSave.action'
    data = {
        "mdEquipmentName": mdEquipmentName,
        "gid": gid,
        "mdEquipmentCode": mdEquipmentCode,
        "cycle": cycle,
        "imeOverhaulPlanType": imeOverhaulPlanType,
        "imeOverhaulBillSpareList": [],
        "endDate": endDate,
        "cycleUnit": cycleUnit,
        "mdEquipmentGid": mdEquipmentGid,
        "code": code,
        "startDate": startDate,
        "smPersonnelName": smPersonnelName,
        # "mdEquipmentSpec": mdEquipmentSpec,
        "mdEquipmentModel": mdEquipmentModel,
        "status": status,
        "imeOverhaulPlanGid": imeOverhaulPlanGid,
        "imeOverhaulBillInfoList":[{
            "standard": standard,
            "gid": obilgid,
            "imeOverhaulBillGid": imeOverhaulBillGid,
            "imeOverhaulPlanInfoGid": imeOverhaulPlanInfoGid,
            "content": content,
            "result": "大修结果"
        }],
        "imeOverhaulPlanCode": imeOverhaulPlanCode,
        "smPersonnelGid": smPersonnelGid
    }
    obrreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return obrreq
