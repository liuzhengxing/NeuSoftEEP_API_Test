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


def lcl_data_order(sheet, row):
    time.sleep(1)
    ordercode = "IT_PO_" + str(time.time())
    print(ordercode)
    dl = lcl_data(sheet, row)
    dl['code'] = ordercode
    # print(dl)
    return dl


def order_create(data):
    """订单—创建"""
    url = BaseUrl + '/ime-container/imePlanOrder/insertPlanOrder.action'
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def order_modify(data):
    """订单-修改"""
    url = BaseUrl + '/ime-container/imePlanOrder/modifyPlanOrder.action'
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def order_layout(gidlist):
    """订单-编排预览"""
    url = BaseUrl + '/ime-container/imePlanOrder/sortPlanOrder.action'
    sends = {
        "gids": gidlist,
        "data": [
            {
                "filedCode":  "plan_qty",
                "filedRule":  "desc"
            },
            {
                "filedCode":  "code",
                "filedRule":  "asc"
            }
        ]
    }
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(sends)).content.decode()
        return req
    except Exception as e:
        return e


def order_changestatut(gidlist):
    """订单-修改状态"""
    url = BaseUrl + '/ime-container/imePlanOrder/releasePlanOrderChangeStatut.action'
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(gidlist)).content.decode()
        return req
    except Exception as e:
        return e


def order_release(gidlist):
    """订单-下发"""
    url = BaseUrl + '/ime-container/imePlanOrder/releasePlanOrder.action'
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(gidlist)).content.decode()
        return req
    except Exception as e:
        return e


def order_batch(gid, blist):
    """订单-分单"""
    url = BaseUrl + '/ime-container/imePlanOrder/planOrderBatch.action'
    bdata = [{
        'orderGid': gid,
        'batchQtyResults': blist
    }]
    print(bdata)
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(bdata)).content.decode()
        return req
    except Exception as e:
        return e


def order_merge(gidlist):
    """订单-合单"""
    url = BaseUrl + '/ime-container/imePlanOrder/planOrderMerge.action'
    try:
        req = requests.post(url=url, headers=headers, data=json.dumps(gidlist)).content.decode()
        return req
    except Exception as e:
        return e


if __name__ == '__main__':
    data = get_data(0, 1)
    res = order_create(**data)
    print(res)
