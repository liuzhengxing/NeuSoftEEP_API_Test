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


def repairbill_create():
    u'''创建维修单'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeRepairBill/save.action'
    data = {
        "mdEquipmentGid": excel.excel_find('EquipmentGid'),
        "mdEquipmentGidRef": {"name": "设备1", "spec": "", "model": "autotest", "code": "autotest1"},
        "imeRepairBillDetailList": [
            {
                "eventPayload": {},
                "repairDuration": "8h",
                "errorDescription": "故障描述",
                "errorType": "mechanical_error",
                "errorLevel": "high"
            }
        ]
    }
    rbcreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    rbgid = json.loads(rbcreq)['data']
    return rbgid


def repairbill_select(rbgid):
    u'''查询维修单详情'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeRepairBill/findById.action?gid=' + rbgid
    rbsreq = requests.get(interfaceurl, headers=headers).content.decode()
    return rbsreq


def repairbill_find(key):
    u'''维修单高级查询'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeRepairBill/query.action'
    data = {"query":{
        "query":[
            {"left":"(","field":"code","type":"like","value":key,"operator":"or"},
            {"field":"mdEquipmentGidRef.code","type":"like","value":key,"operator":"or"},
            {"field":"mdEquipmentGidRef.name","type":"like","value":key,"operator":"or"},
            {"field":"mdEquipmentGidRef.spec","type":"like","value":key,"operator":"or"},
            {"field":"mdEquipmentGidRef.model","type":"like","value":key,"operator":"or"},
            {"field":"applyDepartmentName","type":"like","value":key,"operator":"or"},
            {"field":"applyPersonnelName","type":"like","value":key,"operator":"or"},
            {"right":")","field":"status","type":"like","value":key,"operator":"and"}
        ]},
        "pager":{"page":1,"pageSize":10}
    }
    rbfreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return rbfreq


def repairbill_submit(rbgids):
    u'''提交维修单'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeRepairBill/batchApply.action'
    rbsureq = requests.post(interfaceurl, headers=headers, data=json.dumps(rbgids)).content.decode()
    return rbsureq


def repairbill_dispatch(rbgids):
    u'''维修单派工'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeRepairBill/assignRepair.action'
    data = {
        "ids": rbgids,
        "repairPersonnelName": "接口自动化测试人员",
        "repairPersonnelGid": excel.excel_find('PersonnelGid')}
    rbsureq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return rbsureq


def repairbill_saveorrecord(rbgid, action):
    u'''维修单报工/保存报工'''
    rbsreq = repairbill_select(rbgid)
    rbsjson = json.loads(rbsreq)['data']
    ecode = rbsjson['mdEquipmentGidRef']['code']
    ename = rbsjson['mdEquipmentGidRef']['name']
    emodel = rbsjson['mdEquipmentGidRef']['model']
    # espec = rbsjson['mdEquipmentGidRef']['spec']
    mdEquipmentGid = rbsjson['mdEquipmentGid']
    code = rbsjson['code']
    repairPersonnelGid = rbsjson['repairPersonnelGid']
    repairPersonnelName = rbsjson['repairPersonnelName']
    status = rbsjson['status']
    rbdrepairDuration = rbsjson['imeRepairBillDetailList'][0]['repairDuration']
    rbderrorType = rbsjson['imeRepairBillDetailList'][0]['errorType']
    rbdgid = rbsjson['imeRepairBillDetailList'][0]['gid']
    rbdcode = rbsjson['imeRepairBillDetailList'][0]['code']
    rbdimeRepairBillGid = rbsjson['imeRepairBillDetailList'][0]['imeRepairBillGid']
    rbderrorLevel = rbsjson['imeRepairBillDetailList'][0]['errorLevel']
    rbdrepairStatus = rbsjson['imeRepairBillDetailList'][0]['repairStatus']
    rbderrorDescription = rbsjson['imeRepairBillDetailList'][0]['errorDescription']
    data = {
        "imeRepairBillSpareList": [],
        "gid": rbgid,
        "imeRepairBillDetailList": [{
            "repairDuration": rbdrepairDuration,
            "errorType": rbderrorType,
            "gid": rbdgid,
            "repairBeginTime": "2018-03-01 10:02:08",
            "code": rbdcode,
            "imeRepairBillGid": rbdimeRepairBillGid,
            "errorDescription": rbderrorDescription,
            "errorProcessingResult": "故障分析及内容",
            "repairEndTime": "2018-03-02 10:02:11",
            "errorLevel": rbderrorLevel,
            "repairStatus": rbdrepairStatus
        }],
        "mdEquipmentGidRef": {
            "code": ecode,
            "name": ename,
            "model": emodel,
            # "spec": espec
        },
        "mdEquipmentGid": mdEquipmentGid,
        "code": code,
        "repairPersonnelGid": repairPersonnelGid,
        "status": status,
        "repairPersonnelName": repairPersonnelName
    }
    interfaceurl = ''
    if action == 'record':
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeRepairBill/report.action'
    elif action == 'save':
        interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeRepairBill/reportSave.action'
    rbrreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return rbrreq
