# _*_ coding:utf-8 _*_

import unittest

from unittest.mock import Mock

from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.工单 import WorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.生产工艺 import ProdRouteLine
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.派工单 import TrackOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.报工 import ReportOrder
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code
from public import params


class TestReportOrderReport(unittest.TestCase):
    """报工测试类"""

    def setUp(self):
        self.wo = WorkOrder()
        self.prl = ProdRouteLine()
        self.to = TrackOrder()
        self.ro = ReportOrder()
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
        self.report_mock_data = {
            "reportOrderId": "",    # 工单id或派工单id 必填
            "resourceOrderType": "",    # 报工类型 10020工单直接报工,reportOrderId为工单id 10030派工单报工,reportOrderId为派工单id,必填
            "imeReportOrderOperations": [
                    # {
                    #     "operationGid": 1,  # 当前报工工序id,10020工单直接报工,operationGid为工单工艺工序id或工序主数据id,10030派工单报工，operationGid为派工单工序id，必填
                    #     "curQualifiedQty": 1,   # 良品数量
                    #     "curRepairQty": 1  # 不良品数量  良品数量和不良品数量必须有一个必填，且大于0
                    # }
                ]
        }
        self.track_mock_data = [{
            "orderId": "123",  # 工单ID
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
        self.track_query_data = {
            "query": {
                "query": [
                    # {
                    #     "field": "smBusiUnitGid",
                    #     "type": "eq",
                    #     "value": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
                    #     "operator": "and"
                    # },
                    {
                        "operator": "and",
                        "field": "workOrderRef.code",
                        "type": "eq",
                        "value": "ssssssssssssssssssssss",
                        "left": "(",
                        "right": ")"
                    }
                ]
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }
        self.track_assign_data = {
            "gid": '',
            'workUnitGid': '',
            'imeTrackOrderOperationList': []
        }

    def test_reportorder_report_1(self):
        """报工接口测试：全部良品报工"""

        # 工单创建
        code = 'WO' + create_code()
        self.workOrder_mock_data['code'] = code
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
        self.to.trackorder_createByWorkOrder = Mock(side_effect=self.to.trackorder_createByWorkOrder)
        resp = self.to.trackorder_createByWorkOrder(self.track_mock_data)

        # 派工单查询
        self.track_query_data.get('query').get('query')[0]['value'] = code
        self.to.trackorder_findByWorkOrderGid = Mock(side_effect=self.to.trackorder_findByWorkOrderGid)
        resp = self.to.trackorder_findByWorkOrderGid(self.track_query_data)
        trackList = resp.pop('data')
        track = trackList[0]

        # 派工及报工参照拼接
        imeTrackOrderOperationList = []
        imeReportOrderOperationsList = []
        for trackOrderOperation in track.get('imeTrackOrderOperationList'):
            tooGid = trackOrderOperation.get('gid')
            toot = {
                'gid': tooGid,
                'curTrackQty': 10
            }
            imeTrackOrderOperationList.append(toot)
            toor = {
                'operationGid': tooGid,
                'curQualifiedQty': 10,
                'curRepairQty': 0
            }
            imeReportOrderOperationsList.append(toor)

        trackGid = track.get('gid')
        self.track_assign_data['gid'] = trackGid
        self.track_assign_data['workUnitGid'] = params.bmFactoryWorkUnitCF
        self.track_assign_data['imeTrackOrderOperationList'] = imeTrackOrderOperationList

        self.report_mock_data['reportOrderId'] = trackGid
        self.report_mock_data['imeReportOrderOperations'] = imeReportOrderOperationsList
        self.report_mock_data['resourceOrderType'] = 10030

        self.to.trackorder_assign = Mock(side_effect=self.to.trackorder_assign)
        resp = self.to.trackorder_assign(self.track_assign_data)

        self.ro.reportorder_report = Mock(side_effect=self.ro.reportorder_report)
        resp = self.ro.reportorder_report(self.report_mock_data)

        # 验证报工记录为3条
        self.assertEqual(3, len(resp.pop('data')))

    def test_reportorder_report_2(self):
        """报工接口测试：全部不良品报工"""

        # 工单创建
        code = 'WO' + create_code()
        self.workOrder_mock_data['code'] = code
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
        self.to.trackorder_createByWorkOrder = Mock(side_effect=self.to.trackorder_createByWorkOrder)
        resp = self.to.trackorder_createByWorkOrder(self.track_mock_data)

        # 派工单查询
        self.track_query_data.get('query').get('query')[0]['value'] = code
        self.to.trackorder_findByWorkOrderGid = Mock(side_effect=self.to.trackorder_findByWorkOrderGid)
        resp = self.to.trackorder_findByWorkOrderGid(self.track_query_data)
        trackList = resp.pop('data')
        track = trackList[0]

        # 派工及报工参照拼接
        imeTrackOrderOperationList = []
        imeReportOrderOperationsList = []
        for trackOrderOperation in track.get('imeTrackOrderOperationList'):
            tooGid = trackOrderOperation.get('gid')
            toot = {
                'gid': tooGid,
                'curTrackQty': 10
            }
            imeTrackOrderOperationList.append(toot)
            toor = {
                'operationGid': tooGid,
                'curQualifiedQty': 0,
                'curRepairQty': 10
            }
            imeReportOrderOperationsList.append(toor)

        trackGid = track.get('gid')
        self.track_assign_data['gid'] = trackGid
        self.track_assign_data['workUnitGid'] = params.bmFactoryWorkUnitCF
        self.track_assign_data['imeTrackOrderOperationList'] = imeTrackOrderOperationList

        self.report_mock_data['reportOrderId'] = trackGid
        self.report_mock_data['imeReportOrderOperations'] = imeReportOrderOperationsList
        self.report_mock_data['resourceOrderType'] = 10030

        self.to.trackorder_assign = Mock(side_effect=self.to.trackorder_assign)
        resp = self.to.trackorder_assign(self.track_assign_data)

        self.ro.reportorder_report = Mock(side_effect=self.ro.reportorder_report)
        resp = self.ro.reportorder_report(self.report_mock_data)

        # 验证报工记录为3条
        self.assertEqual(3, len(resp.pop('data')))


if __name__ == '__main__':
    unittest.main()
