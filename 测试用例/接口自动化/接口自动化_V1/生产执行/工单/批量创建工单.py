import requests
import json


headers = {
    'Content-Type': 'application/json'
}
url = 'http://192.168.138.132/ime-container/imeWorkOrder/insertWorkOrder.action'

data = {
    "factoryLineGid":"fc6189b6b6c24802ad7c88e11032fc6c",
    "orderType":"62DC90DAFA845CB2E055000000000001",
    "orderTypeRef":{"name":"类型一"},
    "materialRef":{
        "code":"Q00",
        "name":"手机",
        "bmMeasurementUnitGidRef":{"name":"台"},
        "bmMeasurementUnitGid":"6BD20391F1C0496AE055000000000001"
    },
    "code":"WO20180511000027",
    "planBeginTime":"2018-05-01 14:57:03",
    "planQty":"1",
    "workCenterRef":{"workCenterName":"慧聚武汉","workCenterCode":"Q1"},
    "imeWorkOrderBoms":[
        {
            "routeOperationGid":"ae63ce0e15374e18a36cc8033c52230d",
             "routeLineGid":"c34720205fcb4551ae4de015f7ee32ec",
             "orderQty":1,
             "routeOperationName":"CPU",
             "factoryStationRef":{"stationCode":"Q111","gid":"847ff649df39448d9a8be7d243b06011","stationName":"CPU"},
             "reviewGid":'true',
             "routeOperationCode":"Q11",
             "materialRef":{
                 "code":"Q11",
                 "bmMeasurementUnitGidRef":{"englishName":"piece","code":"piece","name":"台"},
                 "name":"CPU",
                 "model":"835",
                 "spec":"ANDRIO",
                 "bmWarehouseGidRef":{}
             },"planQty":1,
             "warehouseRef":{},
             "materialNumber":1,
             "routeLineRef":{"gid":"c34720205fcb4551ae4de015f7ee32ec","code":"Q00","name":"手机"},
             "productNumber":1,
             "factoryStationGid":"847ff649df39448d9a8be7d243b06011",
             "materialGid":"f6ec9bcd69974ee4941ece5cf0e7580f",
             "pickingType":"process_of_acquisition"
         },
        {
            "routeOperationGid":"7386f612c9b8488bb9fd21746e5435f3",
             "routeLineGid":"c34720205fcb4551ae4de015f7ee32ec",
             "orderQty":1,
             "routeOperationName":"主板","factoryStationRef":{"stationCode":"Q112","gid":"404bf633c33d4b0d93c019da732ad82b","stationName":"主板"},
             "reviewGid":'false',
             "routeOperationCode":"Q12",
             "materialRef":{
                 "code":"Q12",
                 "bmMeasurementUnitGidRef":{"englishName":"piece","code":"piece","name":"台"},
                 "name":"主板",
                 "model":"RFR1234FE",
                 "spec":"DF32YJ23",
                 "bmWarehouseGidRef":{}
             },
             "planQty":1,
             "warehouseRef":{},
             "materialNumber":1,
             "routeLineRef":{"gid":"c34720205fcb4551ae4de015f7ee32ec","code":"Q00","name":"手机"},
             "productNumber":1,
             "factoryStationGid":"404bf633c33d4b0d93c019da732ad82b",
             "materialGid":"3ed2957d92cc4669b7cd5ecd49afee9a",
             "pickingType":"process_of_acquisition"
         },
        {
            "routeOperationGid":"e51ada23c2164f27b04ffc29808e3c89",
            "routeLineGid":"c34720205fcb4551ae4de015f7ee32ec",
            "orderQty":1,
            "routeOperationName":"屏幕",
            "factoryStationRef":{"stationCode":"Q112","gid":"404bf633c33d4b0d93c019da732ad82b","stationName":"主板"},
            "reviewGid":'false',
            "routeOperationCode":"Q13",
            "materialRef":{
                "code":"Q13",
                "bmMeasurementUnitGidRef":{"englishName":"piece","code":"piece","name":"台"},
                "name":"屏幕",
                "model":"GHR23",
                "spec":"JMTY564",
                "bmWarehouseGidRef":{}
            },"planQty":1,
            "warehouseRef":{},
            "materialNumber":1,
            "routeLineRef":{"gid":"c34720205fcb4551ae4de015f7ee32ec","code":"Q00","name":"手机"},
            "productNumber":1,
            "factoryStationGid":"404bf633c33d4b0d93c019da732ad82b",
            "materialGid":"600582608e384780bdb3020fe326798d",
            "pickingType":"process_of_acquisition"
        }
    ],
    "productGid":"980463064ebc412bb753b1398f00317b",
    "factoryLineRef":{"lineCode":"Q1","lineName":"慧聚重复"},
    "factoryLineType":"REPEAT",
    "smBusiUnitGidRef":{"busiUnitName":"慧聚武汉"},
    "materialGid":"60eb29b9b1de48c1ae085f630ee7970b",
    "smBusiUnitGid":"7640cef103e04ce6a4b3e8c7ce6a1e66",
    "workOrderCategory":"normal",
    "workCenterGid":"6ca3793d487c4d93b50186bc364c89ad",
    "planEndTime":"2018-05-31 14:57:03"
}

data['code'] = 'test'

print(data)