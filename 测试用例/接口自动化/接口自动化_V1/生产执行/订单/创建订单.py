import requests
import json

headers = {
    'Content-Type': 'application/json'
}

url = 'http://192.168.138.132/ime-container/imePlanOrder/insertPlanOrder.action'

for i in range(10000):
    data = {
        "planOrderCategory": "normal",
        "factoryLineGid": "fc6189b6b6c24802ad7c88e11032fc6c",
        "orderType": "62DC90DAFA845CB2E055000000000001",
        "orderTypeRef": {"name": "类型一"},
        "materialRef": {"code": "per10", "name": "性能测试10"},
        "code": "Q20180514" + str(i),
        "planBeginTime": "2018-05-01 13:52:43",
        "planQty": "1000",
        "workCenterRef": {"workCenterName": "慧聚武汉", "workCenterCode": "Q1"},
        "surplusOrderFlag": 'false',
        "factoryLineRef": {"lineName": "慧聚重复", "lineCode": "Q1", "lineType": "REPEAT"},
        "smBusiUnitGidRef": {"busiUnitName": "慧聚武汉"},
        "materialGid": "a2ef229d40f64512a8a87c299e941936",
        "smBusiUnitGid": "7640cef103e04ce6a4b3e8c7ce6a1e66",
        "workCenterGid": "6ca3793d487c4d93b50186bc364c89ad",
        "planEndTime": "2018-05-02 13:52:43"
    }
    requests.post(url, headers=headers, data=json.dumps(data))
    print(i)
