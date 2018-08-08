import requests
import json


headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }

addurl = 'http://192.168.138.132/ime-container/bmEquipInspectPart/add.action'

for i in range(20):
    data = {
            "partCode": "per" + str(i+1),
            "partName": "性能测试" + str(i+1),
            "partDescription": "润滑均匀，速率平稳"
        }
    requests.post(addurl, headers=headers, data=json.dumps(data))
