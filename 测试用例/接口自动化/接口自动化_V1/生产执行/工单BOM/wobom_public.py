# _*_coding: utf-8_*_

import json

import requests

from public import params
from 测试用例.接口自动化.接口自动化_V1.公共部分.lcldata import lcl_data

BaseUrl = params.BaseUrl
ParaDir = params.ParaFile


headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


# def lcl_data_workorderbom(sheet, row):
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


def wobom_allot(wogidlist):
    """自动关联工单BOM"""
    url = BaseUrl + '/ime-container/imeWorkOrderBom/allotWorkOrderBom.action'
    data = {"workOrderGids": wogidlist, "fromType": "default"}
    print(data)
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def wobom_manual(wogid):
    """手动关联BOM"""
    url = BaseUrl + '/ime-container/imeWorkOrderBom/saveWorkOrderBom.action'
    bom = lcl_data('WOBOM', 2)
    data = {
            "gid": "",
            "baseQuantity": "",
            "bomType": "",
            "replaceBom": "",
            "imeWorkOrderGid": wogid,
            "virtual": "false",
            "pivotal": "false",
            "version": "",
            "imeWorkOrderBomDetailList": [
                bom
            ]
        }
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


def wobom_query(wogid):
    url = BaseUrl + '/ime-container/imeWorkOrderBom/query.action?usedPost=true'
    data = {
        "query": {
            "query": [
                {
                    "field": "imeWorkOrderGid",
                    "type": "eq",
                    "value": wogid,
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