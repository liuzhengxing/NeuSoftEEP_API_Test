# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class WorkOrder:
    """
    工单类
    """

    def workorder_create(self, data):
        """
        工单创建接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'code': {'type': 'string'},
        #         'resourceOrderGid': {'type': 'number'},
        #         'workCenterGid': {'type': 'string'},
        #         'orderType': {'type': 'string'},
        #         'materialGid': {'type': 'string'},
        #         'routeLineGid': {'type': 'string'},
        #         'planQty': {'type': 'integer'},
        #         'factoryLineGid': {'type': 'string'},
        #         'planBeginTime': {'type': 'string'},
        #         'planEndTime': {'type': 'string'},
        #         'actualBeginTime': {'type': 'string'},
        #         'actualEndTime': {'type': 'string'},
        #         'finishQty': {'type': 'integer'},
        #         'measureBeginTime': {'type': 'string'},
        #         'measureEndTime': {'type': 'string'},
        #         'orderSeq': {'type': 'string'},
        #         'parentWorkOrderGid': {'type': 'string'},
        #         'freezeStatus': {'type': 'string'},
        #         'orderStatus': [],
        #         'bomStatus': {'type': 'boolean'},
        #         'createStatus': {'type': 'string'},
        #         'roundNum': {'type': 'string'},
        #         'processStatus': [],
        #         'createKmFlag': {'type': 'boolean'},
        #         'createQacFlag': {'type': 'boolean'},
        #         'repairCardGid': {'type': 'string'},
        #         'measurementUnitGid': {'type': 'string'},
        #         'materialVersion': {'type': 'string'},
        #         'busiActivityType': {'type': 'string'},
        #         'qualifiedQty': {'type': 'integer'},
        #         'unqualifiedQty': {'type': 'integer'},
        #         'wasteQty': {'type': 'integer'},
        #         'batchNumber': {'type': 'integer'},
        #         'productGid': {'type': 'string'},
        #         'workOrderCategory': [],
        #         'bomVersion': {'type': 'string'},
        #         'routeLineVersion': {'type': 'string'},
        #         'canOperation': {'type': 'string'},
        #         'surplusOrderFlag': {'type': 'string'},
        #         'publishedQty': {'type': 'integer'},
        #         'factoryLineType': {'type': 'string'},
        #         'generatedCode': {'type': 'string'},
        #
        #     },
        #     'required': [
        #         'code',
        #         'factoryLineGid',
        #         'workCenterGid',
        #         'orderType',
        #         'materialGid',
        #         'planQty',
        #         'planBeginTime',
        #         'planEndTime'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/insertWorkOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_modify(self, data):
        """
        工单更新接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gid': {'type': 'string'},
        #         'code': {'type': 'string'},
        #         'resourceOrderGid': {'type': 'number'},
        #         'workCenterGid': {'type': 'string'},
        #         'orderType': {'type': 'string'},
        #         'materialGid': {'type': 'string'},
        #         'routeLineGid': {'type': 'string'},
        #         'planQty': {'type': 'integer'},
        #         'factoryLineGid': {'type': 'string'},
        #         'planBeginTime': {'type': 'string'},
        #         'planEndTime': {'type': 'string'},
        #         'actualBeginTime': {'type': 'string'},
        #         'actualEndTime': {'type': 'string'},
        #         'finishQty': {'type': 'integer'},
        #         'measureBeginTime': {'type': 'string'},
        #         'measureEndTime': {'type': 'string'},
        #         'orderSeq': {'type': 'string'},
        #         'parentWorkOrderGid': {'type': 'string'},
        #         'freezeStatus': {'type': 'string'},
        #         'orderStatus': [],
        #         'bomStatus': {'type': 'boolean'},
        #         'createStatus': {'type': 'string'},
        #         'roundNum': {'type': 'string'},
        #         'processStatus': [],
        #         'createKmFlag': {'type': 'boolean'},
        #         'createQacFlag': {'type': 'boolean'},
        #         'repairCardGid': {'type': 'string'},
        #         'measurementUnitGid': {'type': 'string'},
        #         'materialVersion': {'type': 'string'},
        #         'busiActivityType': {'type': 'string'},
        #         'qualifiedQty': {'type': 'integer'},
        #         'unqualifiedQty': {'type': 'integer'},
        #         'wasteQty': {'type': 'integer'},
        #         'batchNumber': {'type': 'integer'},
        #         'productGid': {'type': 'string'},
        #         'workOrderCategory': [],
        #         'bomVersion': {'type': 'string'},
        #         'routeLineVersion': {'type': 'string'},
        #         'canOperation': {'type': 'string'},
        #         'surplusOrderFlag': {'type': 'string'},
        #         'publishedQty': {'type': 'integer'},
        #         'factoryLineType': {'type': 'string'},
        #         'generatedCode': {'type': 'string'},
        #
        #     },
        #     'required': [
        #         'gid',
        #         'code',
        #         'factoryLineGid',
        #         'workCenterGid',
        #         'orderType',
        #         'materialGid',
        #         'planQty',
        #         'planBeginTime',
        #         'planEndTime'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/modifyWorkOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_insertByPlanOrder(self, data):
        """
        生产订单转换工单并保存接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array',
        #     'items': {
        #         "type": "object",
        #         'properties': {
        #             'gid': {'type': 'string'},
        #             'refCreateQty': {'type': 'number'}
        #         },
        #         'required': [
        #             'gid',
        #             'refCreateQty'
        #         ]
        #     }
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/insertWorkOrderByPlanOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_sort(self, data):
        """
        编排工单-字段组合接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gids': {'type': 'array'},
        #         'rules': {
        #             'type': 'array',
        #             'items': {
        #                 "type": "object",
        #                 'properties': {
        #                     'filedCode': ['plan_qty', 'code'],
        #                     'filedRule': ['desc', 'asc']
        #                 },
        #             }
        #         }
        #     },
        #     'required': [
        #         'gid',
        #         'rules'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/sortWorkOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_saveSort(self, data):
        """
        更新工单顺序接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'factoryLineGid': {'type': 'string'},
        #         'ids': {'type': 'array'}
        #     },
        #     'required': [
        #         'factoryLineGid',
        #         'ids'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/saveWorkOrderSort.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_release(self, data):
        """
        下发工单并生成派工单接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/releaseWorkOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_changeStatut(self, data):
        """
        下发工单接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/releaseWorkOrderChangeStatut.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_batch(self, data):
        """
        工单分单并保存接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array',
        #     'items': {
        #         "type": "object",
        #         'properties': {
        #             'orderGid': {'type': 'string'},
        #             'batchQtyResults': {'type': 'array'}
        #         },
        #         'required': [
        #             'orderGid',
        #             'batchQtyResults'
        #         ]
        #
        #     }
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/workOrderBatch.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_merge(self, data):
        """
        工单合单并保存接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/workOrderMerge.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_batchCancel(self, data):
        """
        工单撤销分批接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/batchCancel.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_tree(self, data):
        """
        工单树接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/getWorkOrderTree.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def workorder_freezeAll(self, data):
        """
        工单整单冻结接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/freezeAll.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_unFreezeAll(self, data):
        """
        工单整单激活接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/unFreezeAll.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def workorder_findUnPublishWorkOperation(self, data):
        """
        根据工单查询未下发工序信息
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/findUnPublishWorkOperation.action?workOrderGid=' + data)
        req = nr(**kwargs)
        return req

    def workorder_queryBy_data(self, data):
        """
        查询工单详细信息
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeWorkOrder/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
