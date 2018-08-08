# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class ProdBom:
    """
    生产BOM类
    """

    def prodbom_findByPlanId(self, data):
        """
        订单生产BOM详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdBomInfo/findByPlanId.action?orderGid=' + data)
        req = nr(**kwargs)
        return req

    def prodbom_findByWorkId(self, data):
        """
        工单生产BOM详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdBomInfo/findByWorkId.action?orderGid=' + data)
        req = nr(**kwargs)
        return req

    def prodbom_savePlanBom(self, gid, data):
        """
        创建（更新）订单生产BOM接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gid': {'type': 'string'},
        #         'pivotal': {'type': 'boolean'},
        #         'replaceBom': {'type': 'boolean'},
        #         'startTime': {'type': 'string'},
        #         'endTime': {'type': 'string'},
        #         'baseUnit': {'type': 'string'},
        #         'baseQuantity': {'type': 'integer'},
        #         'version': {'type': 'integer'},
        #         'imepProdBomDetailList': {
        #             'type': 'array',
        #             'items': {
        #                 "type": "object",
        #                 'properties': {
        #                     'gid': {'type': 'string'},
        #                     'rowNumber': {'type': 'string'},
        #                     'imeProdBomInfoGid': {'type': 'string'},
        #                     'bomNumber': {'type': 'integer'},
        #                     'materialGid': {'type': 'string'},
        #                     'materialUnit': {'type': 'string'},
        #                     'parentGid': {'type': 'string'},
        #                     'routeOperationGid': {'type': 'string'},
        #                     'routeOperationCode': {'type': 'string'},
        #                     'routeOperationName': {'type': 'string'},
        #                     'lossRate': {'type': 'string'},
        #                     'materialNumber': {'type': 'integer'},
        #                     'productNumber': {'type': 'integer'},
        #                     'pivotal': {'type': 'boolean'},
        #                     'virtual': {'type': 'boolean'},
        #                     'substitute': {'type': 'boolean'},
        #                     'optional': {'type': 'boolean'},
        #                     'useNumber': {'type': 'integer'},
        #                     'dosageScheme': {'type': 'string'},
        #                     'factoryStationGid': {'type': 'string'},
        #                     'validBeginTime': {'type': 'string'},
        #                     'validEndTime': {'type': 'string'},
        #                     'version': {'type': 'string'},
        #                 },
        #                 'required': [
        #                     'materialGid',
        #                     'dosageScheme'
        #                 ]
        #             }
        #         },
        #     },
        #     'required': [
        #         'baseQuantity'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdBomInfo/savePlanBom.action?orderGid=' + gid)
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def prodbom_saveWorkBom(self, gid, data):
        """
        创建（更新）工单生产BOM接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gid': {'type': 'string'},
        #         'pivotal': {'type': 'boolean'},
        #         'replaceBom': {'type': 'boolean'},
        #         'startTime': {'type': 'string'},
        #         'endTime': {'type': 'string'},
        #         'baseUnit': {'type': 'string'},
        #         'baseQuantity': {'type': 'integer'},
        #         'version': {'type': 'integer'},
        #         'imepProdBomDetailList': {
        #             'type': 'array',
        #             'items': {
        #                 "type": "object",
        #                 'properties': {
        #                     'gid': {'type': 'string'},
        #                     'rowNumber': {'type': 'string'},
        #                     'imeProdBomInfoGid': {'type': 'string'},
        #                     'bomNumber': {'type': 'integer'},
        #                     'materialGid': {'type': 'string'},
        #                     'materialUnit': {'type': 'string'},
        #                     'parentGid': {'type': 'string'},
        #                     'routeOperationGid': {'type': 'string'},
        #                     'routeOperationCode': {'type': 'string'},
        #                     'routeOperationName': {'type': 'string'},
        #                     'lossRate': {'type': 'string'},
        #                     'materialNumber': {'type': 'integer'},
        #                     'productNumber': {'type': 'integer'},
        #                     'pivotal': {'type': 'boolean'},
        #                     'virtual': {'type': 'boolean'},
        #                     'substitute': {'type': 'boolean'},
        #                     'optional': {'type': 'boolean'},
        #                     'useNumber': {'type': 'integer'},
        #                     'dosageScheme': {'type': 'string'},
        #                     'factoryStationGid': {'type': 'string'},
        #                     'validBeginTime': {'type': 'string'},
        #                     'validEndTime': {'type': 'string'},
        #                     'version': {'type': 'string'},
        #                 },
        #                 'required': [
        #                     'materialGid',
        #                     'dosageScheme'
        #                 ]
        #             }
        #         },
        #     },
        #     'required': [
        #         'baseQuantity'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdBomInfo/saveWorkBom.action?orderGid=' + gid)
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def prodbom_allotBomByPlanGids(self, data):
        """
        自动生成订单BOM接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdBomInfo/allotBomByPlanGids.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def prodbom_allotBomByWorkGids(self, data):
        """
        自动生成工单BOM接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeProdBomInfo/allotBomByWorkGids.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
