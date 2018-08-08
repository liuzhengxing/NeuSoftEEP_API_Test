# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class PlanOrder:
    """
    订单类
    """

    def planorder_create(self, data):
        """
        订单创建接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'code': {'type': 'string'},
        #         'workCenterGid': {'type': 'string'},
        #         'orderType': {'type': 'string'},
        #         'materialGid': {'type': 'string'},
        #         'planQty': {'type': 'number'},
        #         'factoryLineGid': {'type': 'string'}
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
        kwargs.setdefault('url', '/ime-container/imePlanOrder/insertPlanOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_modify(self, data):
        """
        订单更新接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gid': {'type': 'string'},
        #         'code': {'type': 'string'},
        #         'workCenterGid': {'type': 'string'},
        #         'orderType': {'type': 'string'},
        #         'materialGid': {'type': 'string'},
        #         'planQty': {'type': 'number'},
        #         'factoryLineGid': {'type': 'string'}
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
        kwargs.setdefault('url', '/ime-container/imePlanOrder/modifyPlanOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_sort(self, data):
        """
        订单编排接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gids': {'type': 'array'},
        #         'filedCode': ['plan_qty', 'code'],
        #         'filedRule': ['desc', 'asc'],
        #     },
        #     'required': [
        #         'gids',
        #         'filedCode',
        #         'filedRule',
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/sortPlanOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_savesort(self, data):
        """
        订单顺序更新接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'workCenterGid': {'type': 'string'},
        #         'ids': ['plan_qty', 'code'],
        #     },
        #     'required': [
        #         'workCenterGid',
        #         'ids',
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/savePlanOrderSort.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_release(self, data):
        """
        下发订单并生成工单接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/releasePlanOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_changeStatut(self, data):
        """
        订单下发接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'workCenterGid': {'type': 'string'},
        #         'ids': ['plan_qty', 'code'],
        #     },
        #     'required': [
        #         'workCenterGid',
        #         'ids',
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/releasePlanOrderChangeStatut.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_batch(self, data):
        """
        订单分单并保存接口
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
        #             'batchQtyResults': {'type', 'array'},
        #         },
        #         'required': [
        #             'orderGid',
        #             'batchQtyResults',
        #         ]
        #     }
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/planOrderBatch.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_merge(self, data):
        """
        订单合单并保存接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/planOrderMerge.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_batchCancel(self, data):
        """
        订单撤销分批接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/batchCancel.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_checkUpdateStatus(self, data):
        """
        订单是否可更新接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/checkUpdateStatus.action?orderGid=' + data)
        req = nr(**kwargs)
        return req

    def planorder_findById(self, data):
        """
        订单详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/findById.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def planorder_revokePublish(self, data):
        """
        订单撤销下发接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/revokePublishPlanOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def planorder_tree(self, data):
        """
        订单树接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/getPlanOrderTree.action?gid=' + data)
        req = nr(**kwargs)
        return req
