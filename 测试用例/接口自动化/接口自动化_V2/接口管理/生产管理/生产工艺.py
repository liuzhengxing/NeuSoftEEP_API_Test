# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class ProdRouteLine:
    """
    生产工艺类
    """

    def prodrouteline_findByPlanId(self, data):
        """
        订单生产工艺详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdRouteLine/findByPlanId.action?orderGid=' + data)
        req = nr(**kwargs)
        return req

    def prodrouteline_findByWorkId(self, data):
        """
        工单生产工艺详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdRouteLine/findByWorkId.action?orderGid=' + data)
        req = nr(**kwargs)
        return req

    def prodrouteline_savePlanRouteLine(self, gid, data):
        """
        创建（更新）订单生产工艺接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'active': {'type': 'boolean'},
        #         'code': {'type': 'string'},
        #         'createBy': {'type': 'string'},
        #         'createTime': {'type': 'string'},
        #         'del': {'type': 'boolean'},
        #         'gid': {'type': 'string'},
        #         'imeProdRouteOperationList': {
        #             'type': 'array',
        #             'items': {
        #                 "type": "object",
        #                 'properties': {
        #                     'active': {'type': 'boolean'},
        #                     'businessMode': {'type': 'array'},
        #                     'code': {'type': 'string'},
        #                     'createBy': {'type': 'string'},
        #                     'createTime': {'type': 'string'},
        #                     'defOperationGid': {'type': 'string'},
        #                     'del': {'type': 'boolean'},
        #                     'factoryLineGid': {'type': 'string'},
        #                     'factoryStationGid': {'type': 'string'},
        #                     'gid': {'type': 'string'},
        #                     'imeProdRouteStepList': {'type': 'array'},
        #                     'name': {'type': 'string'},
        #                     'operationStepFinishFlag': {'type': 'boolean'},
        #                     'processTest': {'type': 'boolean'},
        #                     'processingMode': ['unlimited'],
        #                     'rhythm': {'type': 'integer'},
        #                     'rhythmCount': {'type': 'integer'},
        #                     'rhythmType': ['second', 'minute', 'hour'],
        #                     'routeLineGid': {'type': 'string'},
        #                     'rowNumber': {'type': 'string'},
        #                     'type': ['turning'],
        #                     'updateBy': {'type': 'string'},
        #                     'updateTime': {'type': 'string'},
        #                     'workCenterGid': {'type': 'string'},
        #                     'workUnitGid': {'type': 'string'},
        #                     'worksheetGenarationMode': ['workPublishProduce']
        #                 }
        #             },
        #         },
        #         'name': {'type': 'string'},
        #         'outputNum': {'type': 'integer'},
        #         'produceCycle': {'type': 'integer'},
        #         'produceCycleCount': {'type': 'integer'},
        #         'rhythm': {'type': 'integer'},
        #         'rhythmCount': {'type': 'integer'},
        #         'timeTypeProduceCycle': ['second', 'minute', 'hour'],
        #         'timeTypeRhythm': ['second', 'minute', 'hour'],
        #         'updateBy': {'type': 'string'},
        #         'updateTime': {'type': 'string'},
        #         'version': {'type': 'string'},
        #         'workMode': ["start", "end", "process"]
        #     },
        #     'required': [
        #
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdRouteLine/savePlanRouteLine.action?orderGid=' + gid)
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def prodrouteline_saveWorkRouteLine(self, gid, data):
        """
        创建（更新）工单生产工艺接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'active': {'type': 'boolean'},
        #         'code': {'type': 'string'},
        #         'createBy': {'type': 'string'},
        #         'createTime': {'type': 'string'},
        #         'del': {'type': 'boolean'},
        #         'gid': {'type': 'string'},
        #         'imeProdRouteOperationList': {
        #             'type': 'array',
        #             'items': {
        #                 "type": "object",
        #                 'properties': {
        #                     'active': {'type': 'boolean'},
        #                     'businessMode': {'type': 'array'},
        #                     'code': {'type': 'string'},
        #                     'createBy': {'type': 'string'},
        #                     'createTime': {'type': 'string'},
        #                     'defOperationGid': {'type': 'string'},
        #                     'del': {'type': 'boolean'},
        #                     'factoryLineGid': {'type': 'string'},
        #                     'factoryStationGid': {'type': 'string'},
        #                     'gid': {'type': 'string'},
        #                     'imeProdRouteStepList': {'type': 'array'},
        #                     'name': {'type': 'string'},
        #                     'operationStepFinishFlag': {'type': 'boolean'},
        #                     'processTest': {'type': 'boolean'},
        #                     'processingMode': ['unlimited'],
        #                     'rhythm': {'type': 'integer'},
        #                     'rhythmCount': {'type': 'integer'},
        #                     'rhythmType': ['second', 'minute', 'hour'],
        #                     'routeLineGid': {'type': 'string'},
        #                     'rowNumber': {'type': 'string'},
        #                     'type': ['turning'],
        #                     'updateBy': {'type': 'string'},
        #                     'updateTime': {'type': 'string'},
        #                     'workCenterGid': {'type': 'string'},
        #                     'workUnitGid': {'type': 'string'},
        #                     'worksheetGenarationMode': ['workPublishProduce']
        #                 }
        #             },
        #         },
        #         'name': {'type': 'string'},
        #         'outputNum': {'type': 'integer'},
        #         'produceCycle': {'type': 'integer'},
        #         'produceCycleCount': {'type': 'integer'},
        #         'rhythm': {'type': 'integer'},
        #         'rhythmCount': {'type': 'integer'},
        #         'timeTypeProduceCycle': ['second', 'minute', 'hour'],
        #         'timeTypeRhythm': ['second', 'minute', 'hour'],
        #         'updateBy': {'type': 'string'},
        #         'updateTime': {'type': 'string'},
        #         'version': {'type': 'string'},
        #         'workMode': ["start", "end", "process"]
        #     },
        #     'required': [
        #
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdRouteLine/saveWorkRouteLine.action?orderGid=' + gid)
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def prodrouteline_allotRouteLineByPlanGids(self, data):
        """
        创建（更新）工单生产工艺接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdRouteLine/allotRouteLineByPlanGids.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def prodrouteline_allotRouteLineByWorkGids(self, data):
        """
        创建（更新）工单生产工艺接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdRouteLine/allotRouteLineByWorkGids.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
