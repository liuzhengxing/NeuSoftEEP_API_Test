# _*_coding: utf-8_*_

import json

import requests

from public import params
from 测试用例.接口自动化.接口自动化_V1 import lcl_data

BaseUrl = params.BaseUrl
ParaDir = params.ParaFile


headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


# def lcl_data_orderbom(sheet, row):
#     time.sleep(1)
#     fields = excel_readline(ParaDir, sheet, 1)
#     args = excel_readline(ParaDir, sheet, row)
#     sends = {}
#     for i, field in enumerate(fields[:-1]):
#         sends[fields[i+1]] = args[i+1]
#     dd = json.dumps(sends)
#     dl = json.loads(dd)
#     # print(dl)
#     return dl


def orderbom_allot(wogidlist):
    """自动关联订单BOM"""
    url = BaseUrl + '/ime-container/imePlanOrderBom/savePlanOrderBom.action'
    try:
        req = requests.post(url, headers=headers, data=json.dumps(wogidlist)).content.decode()
        return req
    except Exception as e:
        return e


def orderbom_manual(wogid):
    """手动关联BOM"""
    url = BaseUrl + '/ime-container/imeWorkOrderBom/saveWorkOrderBom.action'
    bom = lcl_data('WOBOM', 2)
    data = {
            "gid": "",
            "baseQuantity": "",
            "bomType": "",
            "replaceBom": "",
            "imePlanOrderGid": wogid,
            "virtual": "false",
            "pivotal": "false",
            "version": "",
            "imePlanOrderBomDetailList": [
                bom
            ]
        }
    try:
        print(data)
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def orderbom_query(ordergid):
    url = BaseUrl + '/ime-container/imePlanOrderBom/query.action?usedPost=true'
    data = {
        "query": {
            "query": [
                {
                    "field": "imePlanOrderGid",
                    "type": "eq",
                    "value": ordergid,
                    "operator": "and"
                }
            ]
        },
        "pager": {
            "page": 1,
            "pageSize": 10
        }
    }
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


if __name__ == '__main__':
    pass
