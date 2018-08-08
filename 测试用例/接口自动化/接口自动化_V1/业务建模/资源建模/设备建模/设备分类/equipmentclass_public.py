# _*_coding:utf-8_*_

import requests
import json

from public import params

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def equipmentclass_create():
    u'''创建设备分类'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/bmEquipmentType/createOrUpdate.action'
    data = {"code": "autotest", "name": "接口自动化_V1"}
    ecreq = requests.get(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return ecreq