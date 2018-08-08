# _*_ coding:utf-8 _*_

from unittest.mock import Mock

from public import params
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.工单 import WorkOrder

workOrder_mock_data = {
            "code": "",
            "resourceOrderGid": "",
            "materialGid": params.MaterielSJGid,
            "orderType": "62DC90DAFA845CB2E055000000000001",
            "workCenterGid": params.bmFactoryWorkCenterGid,
            "factoryLineGid": params.bmFactoryLineCF,
            "routeLineGid": "",
            "planQty": 10,
            "planBeginTime": "2018-05-01",
            "planEndTime": "2018-05-31",
            "actualBeginTime": "",
            "actualEndTime": "",
            "finishQty": "",
            "measureBeginTime": "",
            "measureEndTime": "",
            "orderSeq": "",
            "parentWorkOrderGid": "",
            "freezeStatus": "",
            "orderStatus": "",
            "bomStatus": "",
            "createStatus": "",
            "roundNum": "",
            "processStatus": "",
            "createKmFlag": "",
            "createQacFlag": "",
            "repairCardGid": "",
            "measurementUnitGid": params.bmMeasurementUnitGid,
            "materialVersion": "1",
            "busiActivityType": "",
            "qualifiedQty": "",
            "unqualifiedQty": "",
            "wasteQty": "",
            "batchNumber": "",
            "productGid": "",
            "workOrderCategory": "",
            "bomVersion": "",
            "routeLineVersion": "",
            "canOperation": "",
            "surplusOrderFlag": "",
            "publishedQty": "",
            "factoryLineType": "",
            "generatedCode": ""
        }


def workorder_changestatus():
    # 工单创建
    wo = WorkOrder()
    code = 'WO' + create_code()
    workOrder_mock_data['code'] = code
    wo.workorder_create = Mock(side_effect=wo.workorder_create)
    resp = wo.workorder_create(workOrder_mock_data)
    print('Response：', resp)
    # self.assertEqual(self.po.planorder_create(mock_data), mock_resp)

    workOrderGidList = []
    workOrderGid = resp.pop('data')
    workOrderGidList.append(workOrderGid)

    # 工单下发
    wo.workorder_changeStatut = Mock(side_effect=wo.workorder_changeStatut)
    wo.workorder_changeStatut(workOrderGidList)
    return workOrderGidList
