import json

import requests

from 测试用例.接口自动化.接口自动化_V1.业务建模.资源建模.产品建模.产品管理.查询物料GID import getbomgid

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }

# 添加子物料
addzbomurl = 'http://192.168.138.132/ime-container/bmProductInfo/add.action'

for i in range(1):
    i += 1
    bomgid = getbomgid('per' + str(i))
    bmProductDetialList = []
    for j in range(2000):
        zbomcode = i + 2000 + j
        zbomgid = getbomgid('per' + str(zbomcode))
        pivotal = ''
        if zbomcode % 4 == 0:
            pivotal = 'true'
        else:
            pivotal = 'false'
        bmProductDetial = {
            "substitute": "no",
            "bomNumber": 1,
            "denoNumber": 1,
            "dosageScheme": "BOM_NUMBER",
            "mdMaterialGidRef": {"code": "per" + str(zbomcode), "name": "性能测试" + str(zbomcode)},
            "useNumber": 0,
            "materialGid": zbomgid,
            "pivotal": pivotal,
            "moleculeNumber": 1,
            "validBeginTime": "2018-05-01 13:09:20",
            "validEndTime": "2019-05-04 13:09:20"
        }
        bmProductDetialList.append(bmProductDetial)
    data = {
        "bmProductDetialList": bmProductDetialList,
        "endTime": "2099-12-31",
        "replaceBom": "host_bom",
        "pivotal": 'true',
        "startTime": "2018-05-08 13:08:44",
        "mdMaterialGidRef": {"code": bomgid, "name": "性能测试" + str(i)},
        "version": "1",
        "bomType": "produce_bom",
        "materialGid": bomgid
    }
    requests.post(addzbomurl, headers=headers, data=json.dumps(data))
