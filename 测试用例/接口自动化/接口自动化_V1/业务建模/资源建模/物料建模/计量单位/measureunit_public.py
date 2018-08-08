# _*_coding:utf-8_*_

import requests
import json

from public import params

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def measureunit_create():
    u'''创建计量单位'''
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/bmMeasurementUnit/createOrUpdate.action'
    data = [
        {"type": "pcs", "code": "tai", "name": "台", "englishName": "tai", "conversionFactor": "1"}
    ]
    mucreq = requests.post(interfaceurl, headers=headers, data=json.dumps(data)).content.decode()
    return mucreq


if __name__ == '__main__':
    print(measureunit_create())