# -*- coding:utf-8 -*-

import unittest

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import create_code, get_time

from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.订单 import PlanOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.工单 import WorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.派工单 import TrackOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.生产管理.报工 import ReportOrder

from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物料需求 import MaterialRequirement
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物流单 import Logistics
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.物流单报工 import LogBillReport
from 测试用例.接口自动化.接口自动化_V2.接口管理.物流管理.报工记录 import LogReportRecord

from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.质检工单 import QualityWorkOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.派检单 import TrackQualityOrder
from 测试用例.接口自动化.接口自动化_V2.接口管理.质量管理.报检单 import QualityRecord

from 测试用例.接口自动化.接口自动化_V2.接口管理.业务建模.设备 import Equipments

from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检策略 import InspectStrategy
from 测试用例.接口自动化.接口自动化_V2.接口管理.设备管理.设备点检.点检任务 import InspectTask

from public import params


class TestSmoke(unittest.TestCase):
    """冒烟测试"""

    def setUp(self):
        # 脚本执行开关
        self.run_status = {
            'smoke_production': True,
            'smoke_logistics': True,
            'smoke_quality': True,
            'smoke_equipment': True
        }

        # 订单、工单下发方式：0-下发改变状态；1-下发生成下游数据
        # 质检工单自动生成：0-否；1-是
        self.way_planorder_sendown = 1
        self.way_workorder_sendown = 0
        self.way_quality_autocreate = 1

        self.po = PlanOrder()
        self.wo = WorkOrder()
        self.to = TrackOrder()
        self.ro = ReportOrder()

        self.mr = MaterialRequirement()
        self.lo = Logistics()
        self.lbr = LogBillReport()
        self.lro = LogReportRecord()

        self.qwo = QualityWorkOrder()
        self.qto = TrackQualityOrder()
        self.qro = QualityRecord()

        self.eqm = Equipments()

        self.isy = InspectStrategy()
        self.it = InspectTask()

        self.msg = 'Error'

        self.test_sc_status = False
        self.test_wl_status = False
        self.test_zl_status = False
        self.test_sb_status = False

        self.planOrder_create_data = {
            "planOrderCategory": "normal",
            "factoryLineGid": params.bmFactoryLineCF,
            "orderType": "62DC90DAFA845CB2E055000000000001",
            "orderTypeRef": {
                "name": "类型一"
            },
            "materialRef": {
                "code": "Q01",
                "name": "手机",
                "bmMeasurementUnitGidRef": {
                    "name": "件"
                },
                "bmMeasurementUnitGid": params.bmMeasurementUnitGid
            },
            "code": "sfdsfsdafsdfasfasdf",
            "planBeginTime": "2018-08-02 17:18:47",
            "planQty": "11",
            "workCenterRef": {
                "workCenterName": "小米科技",
                "workCenterCode": "Q1"
            },
            "surplusOrderFlag": "false",
            "factoryLineRef": {
                "lineName": "小米重复",
                "lineCode": "Q11",
                "lineType": "REPEAT"
            },
            "smBusiUnitGidRef": {
                "busiUnitName": "小米科技"
            },
            "materialGid": params.MaterielSJGid,
            "smBusiUnitGid": params.busiUnitGid,
            "workCenterGid": params.bmFactoryWorkCenterGid,
            "planEndTime": "2018-08-24 17:18:47"
        }

        self.wo_query_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": params.busiUnitGid,
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "planOrderRef.code",
                        "type": "eq",
                        "value": "",
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

        self.to_createby_data = [{
            "orderId": "123",  # 工单ID
            "refenceQty": 11,  # 本次参照数量，工单产线类型为重复时，必填，产线类型为离散时，不校验此参数
        }]

        self.to_assign_data = {
            "imeTrackOrderOperationList": [
                {
                    "gid": "23ef1117e6ff4b4fad2cc7b6766ad5cc",
                    "curTrackQty": 11
                },
                {
                    "gid": "321fdfcdc14a4557a4c473aec97075ae",
                    "curTrackQty": 11
                }
            ],
            "gid": "a32b387bdaad4f0d85e260948e4d7a24",
            "workUnitGid": "78ae9666dc974110ad74303bbd5b368e"
        }

        self.to_query_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "workOrderRef.code",
                        "type": "eq",
                        "value": "WO1532061056870",
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

        self.ro_report_data = {
            "reportOrderId": "",
            "resourceOrderType": "10030",
            "imeReportOrderOperations": [
                {
                    "operationGid": "5a814bc4682442d6add2836fe609809d",
                    "curQualifiedQty": "11",
                    "curRepairQty": "0"
                },
                {
                    "operationGid": "5b8b28f5755a4189a1c32385c6af4c96",
                    "curQualifiedQty": "11",
                    "curRepairQty": "0"
                }
            ],
            "smBusiUnitGid": "7e2c4ba1d1f64ad7b214a233c7ebb0fb"
        }

        self.materialReq_mock_data = {
            "gids": [],
            "groupBy": [],
            "orderBy": [],
            "strategys": [],
            "strategyGids": []
        }

        self.materialReq_query_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "factoryStationRef.stationName",
                        "type": "eq",
                        "value": "CPU",
                        "left": "(",
                        "right": ")"
                    }
                ],
                "sorted": "createTime desc"
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

        self.lgis_ref_data = {
            "gids": [],
            "groupBy": [],
            "orderBy": []
        }

        self.lgis_query_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": params.busiUnitGid,
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "imeLogTrackBillDetailList.resourceGidRef.code",
                        "type": "eq",
                        "value": "MR201807230023",
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

        self.lgis_bind_data = {
            'gids': [],
            'bmLogRouteGid': params.bmLogRouteGid
        }

        self.lbr_mock_data = {
            "billGidList": [],
            "operationRuleList": [
                {
                    "bmLogOperationGid": params.bmLogOperationGid,
                    "ruleList": []
                }
            ]
        }

        self.lbr_find_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": params.busiUnitGid,
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "logBillReportList.resourceGidRef.code",
                        "type": "eq",
                        "value": "TB",
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

        self.lrr_query_data = {
            "query": {
                "query": [
                    {
                        "field": "opType",
                        "value": "REPORT",
                        "operator": "and",
                        "type": "eq",
                        "left": "(",
                        "right": ")"
                    },
                    {
                        "operator": "and",
                        "field": "objectGid",
                        "type": "eq",
                        "value": "",
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

        self.eqm_add_data = {
            "bmEquipmentTypeGid": "740a423085c54da9bdb3c28442b0f3c4",
            "bmMeasurementUnitGidRef": {
                "name": "件",
                "code": "Q1"
            },
            "model": "FDASFASDF",
            "name": "",
            "code": "",
            "bmMeasurementUnitGid": "f32a4a41e5834369924c5a9fa9358913",
            "status": "intact",
            "bmFactoryWorkCenterGidRef": {
                "workCenterCode": "Q1",
                "workCenterName": "小米科技"
            },
            "smDepartmentGid": "c72e12eceb4b430cb87af95f962c7edf",
            "smBusiUnitGidRef": {
                "busiUnitName": "小米科技"
            },
            "smBusiUnitGid": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
            "smDepartmentGidRef": {
                "code": "Q11",
                "name": "研发部"
            },
            "bmFactoryWorkCenterGid": "4756b6ee4de24d0b82281af141e64e97"
        }

        self.isy_add_data = [
            {
                "inspectCycle": 5,
                "inspectCycleUnit": "时",
                "bmEquipmentGid": "",
                "bmEquipInspectPartGid": params.bmEquipInspectPartGid,
                "bmEquipInspectItemGid": params.bmEquipInspectItemGid
            }
        ]

        self.it_addf_data = {
            "bmEquipmentGid": "",
            "beginTime": "2017-12-31 11:18:35",
            "endTime": "2018-01-01 11:18:35"
        }

        self.it_track_data = {
            "gids": [],
            "headPersonnelGid": params.smPersonnelGid
        }

        self.it_report_data = {
            "gid": "",
            "inspectResult": "normal",
            "inspectResultDescription": "设备运行正常",
            "reportPersonnelGid": params.smPersonnelGid
        }

        self.qwo_query_data = {
            "query": {
                "query": [
                    {
                        "field": "smBusiUnitGid",
                        "type": "eq",
                        "value": "7e2c4ba1d1f64ad7b214a233c7ebb0fb",
                        "operator": "and"
                    },
                    {
                        "operator": "and",
                        "field": "imeWorkOrderGidRef.code",
                        "type": "eq",
                        "value": "fsdfadasfdasfasf",
                        "left": "(",
                        "right": ")"
                    }
                ],
            },
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }

        self.qto_create_data = {
            "code": "",
            "qcDispatchedQty": "1",
            "mdFactoryWorkStationGid": "",
            "imeQcQualityWayGid": "",
            "surveyor": "",
            "checkBeginTime": "",
            "checkEndTime": "",
            "remarks": "",
            "imeQcQacGid": "",
            "imeQcQacCode": "",
            "mdMaterialGid": "",
            "mdProductInfoGid": "",
            "qcHasDispatchedQty": "",
            "qcHasInspectionQty": "",
            "qcDispatchedPersonGid": ""
        }

        self.qro_create_data = {
            "code": "",
            "qcInspectionQty": "1",
            "imeQcQacBillGid": ""
        }

        self.qro_report_data = {
            "qualifiedQty": 1,
            "unQualifiedQty": "",
            "imeQcQualityGradeGid": "",
            "qcHandleWay": "",
            "gid": ""
        }

    def test_smoke(self):
        ass_module = []
        for module in self.run_status:
            if self.run_status[module]:
                ass_module.append(module)
                eval('self.' + module)()

        if 'smoke_production' in ass_module:
            self.assertEqual(self.test_sc_status, True)
        if 'smoke_logistics' in ass_module:
            self.assertEqual(self.test_wl_status, True)
        if 'smoke_quality' in ass_module:
            self.assertEqual(self.test_zl_status, True)
        if 'smoke_equipment' in ass_module:
            self.assertEqual(self.test_sb_status, True)


        # self.smoke_production()

        # if self.test_sc_status is True and self.test_wl_status is True and self.test_sb_status is True:
        #     self.assertEqual(1, 1)
        # else:
        #     self.assertEqual(1, 2)

    def smoke_production(self):
        """生产流程冒烟"""
        print(get_time(), ' START：生产模块冒烟测试')

        # 创建订单
        po_code = 'PO' + create_code()
        print(get_time(), ' INFO：【生产订单】预创建，编码：', po_code)
        self.planOrder_create_data['code'] = po_code
        try:
            resp_planorder_create = self.po.planorder_create(self.planOrder_create_data)
            if 'code' in resp_planorder_create.keys():
                self.msg = resp_planorder_create.get('message')
            self.assertNotIn('code', resp_planorder_create.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.po_gid = resp_planorder_create.get('data')    # 订单GID
            self.assertNotEqual(self.po_gid, None, msg='ERROR：生产订单创建失败')
            print(get_time(), ' INFO：【生产订单】创建成功，订单GID：', self.po_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 订单下发
        try:
            resp_planorder_release = self.po.planorder_release([self.po_gid])
            if 'code' in resp_planorder_release.keys():
                self.msg = resp_planorder_release.get('message')
            self.assertNotIn('code', resp_planorder_release.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.wo_gid_list = resp_planorder_release.get('data')  # 工单GID
            print(get_time(), ' INFO：【生产订单】下发成功，生产工单GIDList：', self.wo_gid_list)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 查询工单信息获取工单编码
        try:
            self.wo_query_data['query']['query'][1]['value'] = po_code
            resp_wo_query = self.wo.workorder_queryBy_data(self.wo_query_data)
            if 'code' in resp_wo_query.keys():
                self.msg = resp_wo_query.get('message')
            self.assertNotIn('code', resp_wo_query.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('code', resp_wo_query.get('data')[0].keys(), msg=get_time() + ' ERROR：未查询到生产工单信息')
            self.wo_code = resp_wo_query.get('data')[0].get('code')
            print(get_time(), ' INFO：【生产工单】编码：', self.wo_code)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 工单下发方式
        if self.way_workorder_sendown == 0:
            # 工单下发修改状态
            try:
                resp_wo_changestatus = self.wo.workorder_changeStatut(self.wo_gid_list)
                if 'code' in resp_wo_changestatus.keys():
                    self.msg = resp_wo_changestatus.get('message')
                self.assertNotIn('code', resp_wo_changestatus.keys(), msg=get_time() + ' ERROR：' + self.msg)
                self.assertIn('success', resp_wo_changestatus.keys(), msg=get_time() + ' ERROR：【生产工单】下发修改状态失败')
                print(get_time(), ' INFO：【生产工单】下发修改状态成功')
            except Exception as e:
                print(get_time(), ' ERROR：', e)

            # 参照工单生成派工单
            try:
                self.to_createby_data[0]['orderId'] = self.wo_gid_list[0]
                resp_to_createby = self.to.trackorder_createByWorkOrder(self.to_createby_data)
                if 'code' in resp_to_createby.keys():
                    self.msg = resp_to_createby.get('message')
                self.assertNotIn('code', resp_to_createby.keys(), msg=get_time() + ' ERROR：' + self.msg)
                self.assertIn('success', resp_to_createby.keys(), msg=get_time() + ' ERROR：【生产派工单】参照失败')
                print(get_time(), ' INFO：【生产派工单】参照成功')
            except Exception as e:
                print(get_time(), ' ERROR：', e)
        elif self.way_workorder_sendown == 1:
            # 工单下发生成派工单
            try:
                resp_wo_release = self.wo.workorder_release(self.wo_gid_list)
                if 'code' in resp_wo_release.keys():
                    self.msg = resp_wo_release.get('message')
                self.assertNotIn('code', resp_wo_release.keys(), msg=get_time() + ' ERROR：' + self.msg)
                self.assertIn('success', resp_wo_release.keys(), msg=get_time() + ' FAIL：【生产工单】下发失败')
                print(get_time(), ' INFO：【生产工单】下发成功')
            except Exception as e:
                print(get_time(), ' ERROR：', e)

        # 查询派工单
        self.to_query_data['query']['query'][1]['value'] = self.wo_code
        try:
            resp_to_query = self.to.trackorder_queryByData(self.to_query_data)
            if 'code' in resp_to_query.keys():
                self.msg = resp_to_query.get('message')
            self.assertNotIn('code', resp_to_query.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertLess(0, len(resp_to_query.get('data')), msg=get_time() + ' ERROR：未查询到生产派工单信息')
            print(get_time(), ' INFO：【生产派工单】编码：', resp_to_query.get('data')[0].get('code'))
            self.to_gid = resp_to_query.get('data')[0].get('gid')
            self.to_oper_list = resp_to_query.get('data')[0].get('imeTrackOrderOperationList')
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 生产派工
        if self.way_workorder_sendown == 0:
            try:
                i = 0
                self.to_assign_data['gid'] = self.to_gid
                for to_oper in self.to_oper_list:
                    to_oper_gid = to_oper.get('gid')
                    self.to_assign_data['imeTrackOrderOperationList'][i]['gid'] = to_oper_gid
                    i += 1
                resp_to_assign = self.to.trackorder_assign(self.to_assign_data)
                if 'code' in resp_to_assign.keys():
                    self.msg = resp_to_assign.get('message')
                self.assertNotIn('code', resp_to_assign.keys(), msg=get_time() + ' ERROR：' + self.msg)
                self.assertIn('data', resp_to_assign.keys(), msg=get_time() + ' ERROR：生产派工失败')
                print(get_time(), ' INFO：【生产派工】成功')
            except Exception as e:
                print(get_time(), ' ERROR：', e)

        # 生产报工
        self.ro_report_data['reportOrderId'] = self.to_gid
        i = 0
        for imeTrackOrderOperation in self.to_oper_list:
            to_oper_gid = imeTrackOrderOperation.get('gid')
            self.ro_report_data['imeReportOrderOperations'][i]['operationGid'] = to_oper_gid
            i += 1
        try:
            resp_ro_report = self.ro.reportorder_report(self.ro_report_data)
            if 'code' in resp_ro_report.keys():
                self.msg = resp_ro_report.get('message')
            self.assertNotIn('code', resp_ro_report.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_ro_report.keys(), msg=get_time() + ' ERROR：生产报工失败')
            self.assertEqual(2, len(resp_ro_report.get('data')), msg=get_time() + ' ERROR：生产报工失败')
            print(get_time(), ' INFO：【生产派工单】报工成功')
            print(get_time(), ' END：生产模块冒烟成功')
            self.test_sc_status = True
        except Exception as e:
            print(get_time(), ' ERROR：', e)

    def smoke_logistics(self):
        """物流流程冒烟"""
        print(get_time(), ' START：物流模块冒烟测试')

        # 物料需求参照工单生产
        try:
            self.materialReq_mock_data['gids'] = self.wo_gid_list
            resp_mr_rcreate = self.mr.materialmrequirement_referenceGeneration(self.materialReq_mock_data)
            if 'code' in resp_mr_rcreate.keys():
                self.msg = resp_mr_rcreate.get('message')
            self.assertIn('success', resp_mr_rcreate.keys(), msg=get_time() + ' ERROR：' + self.msg)
            print(get_time(), ' INFO：物料需求创建成功')
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 查询物料需求
        try:
            resp_rm_query = self.mr.materialmrequirement_queryByData(self.materialReq_query_data)
            if 'code' in resp_rm_query.keys():
                self.msg = resp_rm_query.get('message')
            self.assertNotIn('code', resp_rm_query.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertLess(0, len(resp_rm_query.get('data')), msg=get_time() + ' ERROR：未查询到物料需求单')
            self.mr_code = resp_rm_query.get('data')[0].get('code')
            self.mr_gid = resp_rm_query.get('data')[0].get('gid')
            print(get_time(), ' INFO：物料需求单编码：', self.mr_code)
            print(get_time(), ' INFO：物料需求单GID：', self.mr_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 参照生成物流单
        try:
            mr_gid_list = []
            mr_gid_list.append(self.mr_gid)
            self.lgis_ref_data['gids'] = mr_gid_list
            resp_lo_rcreate = self.lo.logistics_referenceGeneration(self.lgis_ref_data)
            if 'code' in resp_lo_rcreate.keys():
                self.msg = resp_lo_rcreate.get('message')
            self.assertIn('success', resp_lo_rcreate.keys(), msg=get_time() + ' ERROR：' + self.msg)
            print(get_time(), ' INFO：物料单创建成功')
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 查询物流单
        try:
            self.lgis_query_data['query']['query'][1]['value'] = self.mr_code
            resp_lo_query = self.lo.logistics_queryByData(self.lgis_query_data)
            if 'code' in resp_lo_query.keys():
                self.msg = resp_lo_query.get('message')
            self.assertNotIn('code', resp_lo_query.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertLess(0, len(resp_lo_query.get('data')), msg=get_time() + ' ERROR：未查询到物流单')
            self.lo_gid = resp_lo_query.get('data')[0].get('gid')
            self.lo_code = resp_lo_query.get('data')[0].get('code')
            print(get_time(), ' INFO：物料流单编码：', self.lo_code)
            print(get_time(), ' INFO：物料流单GID：', self.lo_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 设置物流单工艺模板
        try:
            self.lg_list = []
            self.lg_list.append(self.lo_gid)
            self.lgis_bind_data['gids'] = self.lg_list
            resp_lo_bind = self.lo.logistics_bindLogRoute(self.lgis_bind_data)
            if 'code' in resp_lo_bind.keys():
                self.msg = resp_lo_bind.get('message')
            self.assertNotIn('code', resp_lo_bind.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('success', resp_lo_bind.keys(), msg=get_time() + ' ERROR：物流单工艺模板设置失败')
            print(get_time(), ' INFO：物流单工艺模板设置成功')
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 创建物流报工单
        try:
            self.lbr_mock_data['billGidList'] = self.lg_list
            resp_lbr_createb = self.lbr.logbillreport_createByTrackBill(self.lbr_mock_data)
            if 'code' in resp_lbr_createb.keys():
                self.msg = resp_lbr_createb.get('message')
            self.assertNotIn('code', resp_lbr_createb.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('success', resp_lbr_createb.keys(), msg=get_time() + ' ERROR：物流报工单创建失败')
            self.assertLess(0, len(resp_lbr_createb.get('data')), msg=get_time() + ' ERROR：物流报工单创建失败')
            self.lbr_gid_list = resp_lbr_createb.get('data')
            print(get_time(), ' INFO：物流报工单GIDList：', self.lbr_gid_list)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 整单报工
        try:
            resp_lbr_report = self.lbr.logbillreport_reportByBill(self.lbr_gid_list)
            if 'code' in resp_lbr_report.keys():
                self.msg = resp_lbr_report.get('message')
            self.assertNotIn('code', resp_lbr_report.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('success', resp_lbr_report.keys(), msg=get_time() + ' ERROR：物流报工失败')
            print(get_time(), ' INFO：物流报工成功')
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 查询物流报工记录
        try:
            self.lrr_query_data['query']['query'][1]['value'] = self.lbr_gid_list[0]
            resp_lrr_query = self.lro.logreportrecord_query(self.lrr_query_data)
            if 'code' in resp_lrr_query.keys():
                self.msg = resp_lrr_query.get('message')
            self.assertNotIn('code', resp_lrr_query.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertEqual(1, len(resp_lrr_query.get('data')))
            print(get_time(), ' INFO：查询到物流报工记录')
            print(get_time(), ' END：物流模块冒烟成功')
            self.test_wl_status = True
        except Exception as e:
            print(get_time(), ' ERROR：', e)

    def smoke_equipment(self):
        """设备流程冒烟"""
        print(get_time(), ' START：设备模块冒烟测试')
        print(get_time(), ' START：设备点检冒烟测试')

        # 创建设备
        try:
            self.eqm_add_data['name'] = 'IT_Equipment_' + create_code()
            self.eqm_add_data['code'] = 'IT_Equipment_' + create_code()
            resp_eqm_add = self.eqm.equipment_create(self.eqm_add_data)
            if 'code' in resp_eqm_add.keys():
                self.msg = resp_eqm_add.get('message')
            self.assertNotIn('code', resp_eqm_add.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_eqm_add.keys(), msg=get_time() + ' ERROR：设备创建失败')
            self.eqm_gid = resp_eqm_add.get('data')
            print(get_time(), ' INFO：设备GID：', self.eqm_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 创建点检策略
        try:
            self.isy_add_data[0]['bmEquipmentGid'] = self.eqm_gid
            resp_isy_add = self.isy.inspectstrategiy_addBatch(self.isy_add_data)
            if 'code' in resp_isy_add.keys():
                self.msg = resp_isy_add.get('message')
            self.assertNotIn('code', resp_isy_add.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_isy_add.keys(), msg=get_time() + ' ERROR：设备点检策略创建失败')
            self.isy_gid = resp_isy_add.get('data')
            print(get_time(), ' INFO：设备点检策略GID：', self.isy_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 点检任务参照策略创建
        try:
            self.it_addf_data['bmEquipmentGid'] = self.eqm_gid
            resp_it_addaf = self.it.inspecttask_addFromInspectStrategy(self.it_addf_data)
            if 'code' in resp_it_addaf.keys():
                self.msg = resp_it_addaf.get('message')
            self.assertNotIn('code', resp_it_addaf.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_it_addaf.keys(), msg=get_time() + ' ERROR：设备点检任务创建失败')
            self.it_gid_list = resp_it_addaf.get('data')
            print(get_time(), ' INFO：设备点检任务GIDList：', self.it_gid_list)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 点检任务派工
        try:
            self.it_track_data['gids'] = self.it_gid_list
            resp_it_track = self.it.inspecttask_track(self.it_track_data)
            if 'code' in resp_it_track.keys():
                self.msg = resp_it_track.get('message')
            self.assertNotIn('code', resp_it_track.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('success', resp_it_track.keys(), msg=get_time() + ' ERROR：点检任务派工失败')
            print(get_time(), ' INFO：点检任务派工成功')
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 点检任务报工
        try:
            self.it_report_data['gid'] = self.it_gid_list[0]
            resp_it_report = self.it.inspecttask_report(self.it_report_data)
            if 'code' in resp_it_report.keys():
                self.msg = resp_it_report.get('message')
            self.assertNotIn('code', resp_it_report.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('success', resp_it_report.keys(), msg=get_time() + ' ERROR：点检任务报工失败')
            print(get_time(), ' INFO：点检任务报工成功')
            print(get_time(), ' END：设备点检冒烟成功')
            self.test_sb_status = True
        except Exception as e:
            print(get_time(), ' ERROR：', e)

    def smoke_quality(self):
        """质量流程冒烟"""
        if self.way_quality_autocreate == 0:
            # 参照生产工单生成质检工单
            try:
                resp_qwo_ref = self.qwo.qualityWorkOrder_ref(self.wo_gid_list)
                if 'code' in resp_qwo_ref.keys():
                    self.msg = resp_qwo_ref.get('message')
                self.assertNotIn('code', resp_qwo_ref.keys(), msg=get_time() + ' ERROR：' + self.msg)
                self.assertIn('success', resp_qwo_ref.keys(), msg=get_time() + ' ERROR：参照工单生成质检工单失败')
                print(get_time(), ' INFO：参照工单生成质检工单成功')
            except Exception as e:
                print(get_time(), ' ERROR：', e)

        # 查询质检工单
        try:
            self.qwo_query_data['query']['query'][1]['value'] = self.wo_code
            resp_qwo_query = self.qwo.qualityWorkOrder_query(self.qwo_query_data)
            if 'code' in resp_qwo_query.keys():
                self.msg = resp_qwo_query.get('message')
            self.assertNotIn('code', resp_qwo_query.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_qwo_query.keys(), msg=get_time() + ' ERROR：质检工单查询失败')
            self.assertLess(0, len(resp_qwo_query.get('data')), msg=get_time() + ' ERROR：未查询到质检工单')
            self.qwo_gid = resp_qwo_query.get('data')[0].get('gid')
            self.qwo_code = resp_qwo_query.get('data')[0].get('code')
            print(get_time(), ' INFO：质检工单GID：', self.qwo_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 生成派检单
        try:
            self.qto_create_data['imeQcQacGid'] = self.qwo_gid
            self.qto_create_data['imeQcQacCode'] = self.qwo_code
            resp_qto_create = self.qto.trackQualityOrder_add(self.qto_create_data)
            if 'code' in resp_qto_create.keys():
                self.msg = resp_qto_create.get('message')
            self.assertNotIn('code', resp_qto_create.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_qto_create.keys(), msg=get_time() + ' ERROR：生成派检单失败')
            self.qto_gid = resp_qto_create.get('data')
            print(get_time(), ' INFO：派检单GID：', self.qto_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 生成报检单
        try:
            self.qro_create_data['imeQcQacBillGid'] = self.qto_gid
            resp_qro_create = self.qro.qualityRecord_add(self.qro_create_data)
            if 'code' in resp_qro_create.keys():
                self.msg = resp_qro_create.get('message')
            self.assertNotIn('code', resp_qro_create.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_qro_create.keys(), msg=get_time() + ' ERROR：生成派检单失败')
            self.qro_gid = resp_qro_create.get('data')
            print(get_time(), ' INFO：报检单GID：', self.qro_gid)
        except Exception as e:
            print(get_time(), ' ERROR：', e)

        # 报检
        try:
            self.qro_report_data['gid'] = self.qro_gid
            resp_qro_report = self.qro.reportRecord(self.qro_report_data)
            if 'code' in resp_qro_report.keys():
                self.msg = resp_qro_report.get('message')
            self.assertNotIn('code', resp_qro_report.keys(), msg=get_time() + ' ERROR：' + self.msg)
            self.assertIn('data', resp_qro_report.keys(), msg=get_time() + ' ERROR：报检失败')
            print(get_time(), ' INFO：报检成功')
            print(get_time(), ' END：物流模块冒烟成功')
            self.test_wl_status = True

        except Exception as e:
            print(get_time(), ' ERROR：', e)


if __name__ == "__main__":
    unittest.main()
