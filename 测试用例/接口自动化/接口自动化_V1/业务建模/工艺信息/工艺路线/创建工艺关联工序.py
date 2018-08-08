import json

import requests
from 测试用例.接口自动化_V1.业务建模.工艺信息.工艺路线.查询工序信息 import get_bmOperationInfo

from 测试用例.接口自动化.接口自动化_V1.业务建模.资源建模.产品建模.产品管理.查询物料GID import getbomgid

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }

addurl = 'http://192.168.138.132/ime-container/bmEquipment/add.action'


for i in range(500):
    num = str(i + 1)
    mdRouteOperList = []
    for j in range(200):
        code = 'per' + str(j+1)
        mdDefOperationGid = get_bmOperationInfo(code)
        mdRouteOper = {
                    "processTest": 'true',
                    "bmWorkUnitGid": "ed308da0c4db48daafb0068392a8c55b",
                    "businessMode": "[]",
                    "bmOperStepList": [],
                    "mdDefOperationGid": mdDefOperationGid,
                    "bmOperationGidRef": {
                        "code": code,
                        "name": "性能测试" + str(j+1),
                        "type": "turning"
                    },
                    "rhythmType": "second",
                    "bmWorkUnitGidRef": {"workUnitName": "总装工作单元"},
                    "rhythm": 1,
                    "processingMode": "unlimited"
                }
        mdRouteOperList.append(mdRouteOper)
    mainMaterieGid = getbomgid('per' + num)
    data = {
        "mode": "addMode",
        "produceCycle": "1",
        "endTime": "2099-12-31",
        "name": "性能测试" + num,
        "timeTypeProduceCycle": "second",
        "code": "per" + num,
        "mainMaterielGidRef": {"code": "per" + num},
        "startTime": "2018-05-01",
        "mainMaterieGid": mainMaterieGid,
        "rhythm": "1",
        "version": "1",
        "timeTypeRhythm": "second",
        "mdRouteOperList": mdRouteOperList
    }
    req = requests.post(addurl, headers=headers, data=json.dumps(data))
    print(req)
