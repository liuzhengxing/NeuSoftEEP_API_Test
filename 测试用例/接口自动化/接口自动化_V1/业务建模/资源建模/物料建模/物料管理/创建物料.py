import requests
import json

url = 'http://192.168.138.132/ime-container/bmMaterielInfo/add.action'
header = {
    'Content-Type': 'application/json;charset=utf-8'
}
i = 0

while True:
    i += 1
    if i == 50000:
        break
    data = {
        "materielTypeGidRef": {"name": "性能测试"},
        "materielTypeGid": "38cb0170af494f9db3d684f411161513",
        "code": "per" + str(i),
        "name": "性能测试" + str(i),
        "versionNumber": "1",
        "homemadePiece": 'true'}
    requests.post(url, headers=header, data=json.dumps(data)).content.decode()
