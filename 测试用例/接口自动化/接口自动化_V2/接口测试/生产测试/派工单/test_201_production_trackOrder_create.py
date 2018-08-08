# _*_ coding:utf-8 _*_

import unittest

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.工单 import WorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.生产工艺 import ProdRouteLine
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.派工单 import TrackOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from public import params


class TestTrackOrderReport(unittest.TestCase):
    """派工单测试类"""

    def setUp(self):
        self.wo = WorkOrder()
        self.prl = ProdRouteLine()
        self.to = TrackOrder()
        self.workOrder_mock_data = {
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
        self.track_mock_data = [{
            "orderId": "123",   # 工单ID
            "refenceQty": 5,  # 本次参照数量，工单产线类型为重复时，必填，产线类型为离散时，不校验此参数
            # "operationList": [   # 本次参照工序，工单产线类型为离散时，必填，产线类型为重复时，不校验此参数
            #     {
            #         "operationId": "op01",  # 工单工艺工序id
            #         "opRefenceQty": "4"     # 本次工序参照数量
            #     },
            #     {
            #         "operationId": "op02",  # 工单工艺工序id
            #         "opRefenceQty": "8"      # 本次工序参照数量
            #     }
            # ]
        }]

    def test_trackorder_create_1(self):
        """派工单创建接口测试：参照工单生成"""

        # 工单创建
        self.wo.workorder_create = Mock(side_effect=self.wo.workorder_create)
        resp = self.wo.workorder_create(self.workOrder_mock_data)
        print('Response：', resp)
        # self.assertEqual(self.po.planorder_create(mock_data), mock_resp)

        workOrderGidList = []
        workOrderGid = resp.pop('data')
        workOrderGidList.append(workOrderGid)

        # 工单下发
        self.wo.workorder_changeStatut = Mock(side_effect=self.wo.workorder_changeStatut)
        self.wo.workorder_changeStatut(workOrderGidList)

        # 派工单参照生成
        self.track_mock_data[0]['orderId'] = workOrderGid
        self.track_mock_data[0]['refenceQty'] = 10
        # operationList = []
        #
        # # 查询工单工艺工序
        # self.prl.prodrouteline_findByWorkId = Mock(side_effect=self.prl.prodrouteline_findByWorkId)
        # resp = self.prl.prodrouteline_findByWorkId(workOrderGid)
        # imeProdRouteOperationList = resp.pop('data').pop('imeProdRouteOperationList')
        # for pro in imeProdRouteOperationList:
        #     operation = {
        #         'operationId': pro.pop('gid'),
        #         'opRefenceQty': 10
        #     }
        #     operationList.append(operation)
        #
        # self.trackOrder_mock_data['operationList'] = operationList

        self.to.trackorder_createByWorkOrder = Mock(side_effect=self.to.trackorder_createByWorkOrder)
        resp = self.to.trackorder_createByWorkOrder(self.track_mock_data)

        # 验证success存在
        self.assertIn('success', resp.keys())

    def test_trackorder_create_2(self):
        """派工单创建接口测试：参照数量大于计划数量"""

        # 工单创建
        self.wo.workorder_create = Mock(side_effect=self.wo.workorder_create)
        resp = self.wo.workorder_create(self.workOrder_mock_data)
        print('Response：', resp)
        # self.assertEqual(self.po.planorder_create(mock_data), mock_resp)

        workOrderGidList = []
        workOrderGid = resp.pop('data')
        workOrderGidList.append(workOrderGid)

        # 工单下发
        self.wo.workorder_changeStatut = Mock(side_effect=self.wo.workorder_changeStatut)
        self.wo.workorder_changeStatut(workOrderGidList)

        # 派工单参照生成
        self.track_mock_data[0]['orderId'] = workOrderGid
        self.track_mock_data[0]['refenceQty'] = 11
        operationList = []

        # 查询工单工艺工序
        # self.prl.prodrouteline_findByWorkId = Mock(side_effect=self.prl.prodrouteline_findByWorkId)
        # resp = self.prl.prodrouteline_findByWorkId(workOrderGid)
        # imeProdRouteOperationList = resp.pop('data').pop('imeProdRouteOperationList')
        # for pro in imeProdRouteOperationList:
        #     operation = {
        #         'operationId': pro.pop('gid'),
        #         'opRefenceQty': 11
        #     }
        #     operationList.append(operation)
        #
        # self.track_mock_data['operationList'] = operationList

        self.to.trackorder_createByWorkOrder = Mock(side_effect=self.to.trackorder_createByWorkOrder)
        resp = self.to.trackorder_createByWorkOrder(self.track_mock_data)

        # 验证异常码为105000
        self.assertEqual(105000, resp.pop('code'))
