# _*_coding:utf-8_*_

import requests
import json

headers = {
    'Content-Type': 'application/json'
}
url = 'http://192.168.138.132/ime-container/bmFactoryWorkStation/add.action'

for i in range(200):
    i = i+42
    if i < 100:
        s = 'x0' + str(i)
    else:
        s = 'x' + str(i)
    print(s)
    data = {"stationCode": s, "stationName": s, "workUnitGid": "bf5cbcfcff5341d29d64a0d97bc4f75e",
            "workUnitGidRef": {"workUnitName": "重复工作单元"}}

    requests.post(url, headers=headers, data=json.dumps(data))

