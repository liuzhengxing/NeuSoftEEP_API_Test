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


# def lcl_data_woroute(sheet, row):
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


def woroute_manule(wogid):
    url = BaseUrl + '/ime-container/imeWorkOrderRouteLine/saveRouteLine.action'
    data = lcl_data('WOROUTE', 2)
    wopress = lcl_data('WOPROCESS', 2)
    wostep = lcl_data('WOSTEP', 2)
    wopress['imeWorkOrderStepsList'] = [wostep]
    data['imeWorkOrderOperationList'] = [wopress]
    data['workOrderGid'] = wogid
    print(data)
    try:
        req = requests.post(url, headers=headers, data=json.dumps(data)).content.decode()
        return req
    except Exception as e:
        return e


if __name__ == '__main__':
    woroute_manule('aaaaaaaaaaaaaaaaaaaaa')
