import requests
import json


headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }

addurl = 'http://192.168.138.132/ime-container/bmEquipment/add.action'


for i in range(200):
    num = str(i + 1)
    data = {
        "code": "per" + num,
        "name": "性能测试" + num,
        "model": "测试" + num,
        "bmEquipmentTypeGid": "4c7879674d5048339a346c05c144765d",
        "bmMeasurementUnitGidRef":
            {"name": "米",
             "code": "UAT_JL-0921"
             },
        "bmMeasurementUnitGid": "858dc0608deb4034833d0abad1f9f31e"
    }
    req = requests.post(addurl, headers=headers, data=json.dumps(data))
    print(req)
