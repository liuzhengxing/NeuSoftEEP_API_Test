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


# def lcl_data_orderroute(sheet, row):
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


def orderroute_manule(ordergid):
    """订单工艺手动关联"""
    url = BaseUrl + '/ime-container/imePlanOrderRouteLine/saveRouteLine.action'
    data = lcl_data('WOROUTE', 2)
    wopress = lcl_data('WOPROCESS', 2)
    wostep = lcl_data('WOSTEP', 2)
    wopress['imePlanOrderWorkStepsList'] = [wostep]
    data['imePlanOrderOperationList'] = [wopress]
    data['imePlanOrderGid'] = ordergid
    print(data)
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


if __name__ == '__main__':
    orderroute_manule('aaaaaaaaaaaaaaaaaaaaa')
