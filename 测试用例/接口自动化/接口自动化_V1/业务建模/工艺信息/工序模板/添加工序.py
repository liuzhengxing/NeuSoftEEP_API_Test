# _*_coding:utf-8_*_

import requests
import json

headers = {
    'Content-Type': 'application/json'
}
url = 'http://192.168.138.132/ime-container/bmOperationInfo/add'

for i in range(100000):
    data = {
        "processTest": 'true',
        "bmWorkUnitGid": "ed308da0c4db48daafb0068392a8c55b",
        "bmWorkCenterGidRef": {"workCenterName": "总装车间"},
        "businessMode": [],
        "name": "性能测试" + str(i+1),
        "code": "per" + str(i+1),
        "rhythmType": "second",
        "bmWorkUnitGidRef": {"workUnitName": "总装工作单元"},
        "rhythm": "1",
        "processingMode": "unlimited",
        "type": "turning"
    }
    requests.post(url, headers=headers, data=json.dumps(data))
