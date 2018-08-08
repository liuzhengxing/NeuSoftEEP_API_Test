from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class TrackOrder:
    """
    派工单类
    """

    def trackorder_create(self, data):
        """
        生产工单转换派工单并保存接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array',
        #     'items': {
        #         'properties': {
        #             'orderId': {'type': 'string'},
        #             'refenceQty': {'type': 'integer'},
        #             'operationList': {
        #                 'type': 'array',
        #                 'items': {
        #                     "type": "object",
        #                     'properties': {
        #                         'operationId': {'type': 'string'},
        #                         'opRefenceQty': {'type': 'number'}
        #                     },
        #                     'required': [
        #                         'operationId',
        #                         'opRefenceQty'
        #                     ]
        #                 }
        #             },
        #         },
        #         'required': [
        #             'orderId',
        #             'operationList'
        #         ]
        #     }
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackOrder/createByWorkOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def trackorder_assign(self, data):
        """
        派工单更新接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gid': {'type': 'string'},
        #         'workUnitGid': {'type': 'number'},
        #         'imeTrackOrderOperationList': {
        #             'type': 'array',
        #             'items': {
        #                 "type": "object",
        #                 'properties': {
        #                     'gid': {'type': 'string'},
        #                     'curTrackQty': {'type': 'number'}
        #                 },
        #                 'required': [
        #                     'gid',
        #                     'curTrackQty'
        #                 ]
        #             }
        #         },
        #     },
        #     'required': [
        #         'orderId',
        #         'operationList'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackOrder/assignTrackOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def trackorder_addEquipmentList(self, data):
        """
        派工单指派设备接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'trackOrderList': {'type': 'array'},
        #         'equipmentList': {'type': 'array'}
        #     }
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackOrder/addEquipmentList.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def trackorder_addPersonList(self, data):
        """
        派工单指派人员接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'trackOrderList': {'type': 'array'},
        #         'personList': {'type': 'array'}
        #     }
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackOrder/addPersonList.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def trackorder_findByWorkOrderGid(self, data):
        """
        异常处置查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'query': {
        #             'type': 'object',
        #             'properties': {
        #                 'query': {
        #                     'type': 'array',
        #                     'items': {
        #                         'type': 'object',
        #                         'properties': {
        #                             'field': ['workOrderGid'],
        #                             'type': ['eq'],
        #                             'value': {'type': 'string'}
        #                         }
        #                     }
        #                 }
        #             }
        #         },
        #         'pager': {
        #             'type': 'object',
        #             'properties': {
        #                 'page': {'type': 'integer'},
        #                 'pageSize': {'type': 'integer'}
        #             }
        #         }
        #
        #     },
        #     'required': [
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackOrder/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def trackorder_createByWorkOrder(self, data):
        """
        生产工单转换派工单并保存接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackOrder/createByWorkOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def trackorder_queryByData(self, data):
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackOrder/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
