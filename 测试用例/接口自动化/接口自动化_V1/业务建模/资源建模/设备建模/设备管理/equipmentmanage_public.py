# _*_coding:utf-8_*_

import requests
import json

from public import params

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def equipment_create():
    u'''创建设备'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/bmEquipment/add.action'
    data = {
        "mdEquipmentTypeGid": "fb004e4e3b794a3b8cca589a31dcaf2f",
        "mdEquipmentTypeGidRef.name": "接口自动化_V1",
        "code": "autotest",
        "name": "接口自动化设备",
        "model": "SB250",
        "bmEquipmentTypeGid": "fb004e4e3b794a3b8cca589a31dcaf2f",
        "bmMeasurementUnitGidRef": {"name": "件", "code": "jian"},
        "bmMeasurementUnitGid": "053b82d9be964b51a5dccd65ab62e9a6"
    }
    mucreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return mucreq


if __name__ == '__main__':
    print(measureunit_create())