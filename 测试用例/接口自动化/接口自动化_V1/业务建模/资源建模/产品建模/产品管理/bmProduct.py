import requests
import json
zwls = []
for i in range(1000):
    zwl = {
                "subTechnicsGid": "60b9a82e19e7400da85868603920ebb8",
                "gid": "625e07ebc0bd4148b899ff6a2f47cb32",
                "lossRate": 0,
                "bomNumber": 1,
                "bmStationRef": {
                    "gid": "2693a8f9b6b544df9cded2420c5a06ad",
                    "stationName": "CPU"
                },
                "denoNumber": 1,
                "validEndTime": "2019-03-01 11:14:36",
                "mdRouteOperationGid": "bd434a796c4a478aaa7756d8a673d08e",
                "bmOperationGidRef": {
                    "gid": "bd434a796c4a478aaa7756d8a673d08e",
                    "name": "CPU"
                },
                "pickWay": "process_of_acquisition",
                "moleculeNumber": 1,
                "mdMaterialGidRef": {
                    "code": "performance" + str(i+1),
                    "bmMeasurementUnitGidRef": {
                        "gid": "86dda764e7954d2280f5d2d49b2d05f8",
                        "name": "件"
                    },
                    "name": "性能测试" + str(i+1),
                    "homemadePiece": 'true',
                    "versionNumber":  str(i+1)
                },
                "bmRouteGidRef": {
                    "gid": "60b9a82e19e7400da85868603920ebb8",
                    "name": "手机重复"
                },
                "useNumber": 1,
                "factoryStationGid": "2693a8f9b6b544df9cded2420c5a06ad",
                "validBeginTime": "2018-03-01 11:14:36",
                "materialGid": "cdf58edef31b4e5eb0f706eae3285e1d",
                "dosageScheme": "BOM_NUMBER"
            }
    zwls.append(zwl)
data = {
    "gid": "f4418be87b554331839cd42d43697ce0",
    "bmProductDetialList": zwls,
    "versionDescription": "1",
    "endTime": "2099-12-31 00:00:00",
    "pivotal": 'true',
    "startTime": "2018-03-01 00:00:00",
    "mdMaterialGidRef": {
        "gid": "0cfc43dc0c2e45e2b200d1fcc18b8eba",
        "code": "performance0001",
        "bmMeasurementUnitGidRef": {
            "gid": "86dda764e7954d2280f5d2d49b2d05f8",
            "name": "件"
        },
        "name": "性能测试0001",
        "bmMeasurementUnitGid": "86dda764e7954d2280f5d2d49b2d05f8"
    },
    "version": "1",
    "bomType": "produce_bom",
    "materialGid": "0cfc43dc0c2e45e2b200d1fcc18b8eba",
    "baseQuantity": 1
}
url = 'http://192.168.138.54:9080/ime-container/bmProductInfo/modify.action'
header = {
    'Content-Type': 'application/json;charset=utf-8'
}
req = requests.post(url, headers=header,data=json.dumps(data))
print(req)