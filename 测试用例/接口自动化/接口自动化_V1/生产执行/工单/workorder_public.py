# _*_coding: utf-8_*_

import json
import time

import requests

from public import params
from 测试用例.接口自动化.接口自动化_V1 import lcl_data

BaseUrl = params.BaseUrl
ParaDir = params.ParaFile


headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def lcl_data_workorder(sheet, row):
    time.sleep(1)
    ordercode = "IT_WO_" + str(time.time())
    print(ordercode)
    dl = lcl_data(sheet, row)
    dl['code'] = ordercode
    # print(dl)
    return dl


def workorder_create(data):
    """工单—创建"""
    url = BaseUrl + '/ime-container/imeWorkOrder/insertWorkOrder.action'
    # print(data)
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def workorder_modify(data):
    """工单-修改"""
    url = BaseUrl + '/ime-container/imeWorkOrder/modifyWorkOrder.action'
    # print(data)
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def workorder_refecreaate(data):
    """工单-参照订单生成"""
    url = BaseUrl + '/ime-container/imeWorkOrder/insertWorkOrderByPlanOrder.action'
    # print(data)
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def workorder_savesort(flgid, wogidlist):
    """工单-编排保存"""
    url = BaseUrl + '/ime-container/imeWorkOrder/saveWorkOrderSort.action?factoryLineGid=' + flgid
    data = {
        "ids": wogidlist,
        "dateStr": "2018-01-01 00:00:00"
    }
    print(url)
    print(data)
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def workorder_release(wogidlist):
    """工单-下发"""
    url = BaseUrl + '/ime-container/imeWorkOrder/releaseWorkOrder.action'
    try:
        req = requests.post(url, headers=headers, data=json.dumps(wogidlist)).content.decode()
        return req
    except Exception as e:
        return e


if __name__ == '__main__':
    pass