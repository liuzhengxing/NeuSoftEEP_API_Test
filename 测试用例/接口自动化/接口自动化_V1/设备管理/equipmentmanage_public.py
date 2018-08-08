# _*_coding: utf-8 _*_

import unittest
import requests
import json

from public import params
from public import excel

domain = params.testdomain
port = params.testport

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


def associationequipment(planSourceGid):
    u'''关联设备'''

    # 关联设备
    interfaceurl = 'http://' + domain + ':' + port + '/ime-container/imeEquipPlanRelation/save.action?gid=' + planSourceGid
    assocdata = [{
        # "gid": "492b0c2d8722445eb0b5dd7febba221c",
        "mdEquipmentGid": excel.excel_find('EquipmentGid'),
        "planSourceGid": planSourceGid,
        "mdEquipmentCode": "autotest1",
        "mdEquipmentName": "设备1",
        "mdEquipmentSpec": "",
        "mdEquipmentModel": "autotest"}]
    areq = requests.post(interfaceurl, headers=headers, data=json.dumps(assocdata)).content.decode()
    return json.loads(areq)['data']


if __name__ == '__main__':
    a = associationequipment('dfa4d9aa34f645c0b2cb4b697cf41504')
