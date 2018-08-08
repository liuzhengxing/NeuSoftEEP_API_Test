# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class Kitting:
    """
    齐套类
    """

    def kitting_bom(self, data):
        """
        BOM齐套接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gidList': {'type': 'array'},
        #         'refType': ['10010', '10020']
        #     },
        #     'required': [
        #         'gidList',
        #         'refType'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeKittingManage/bomKitting.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def kitting_routeLine(self, data):
        """
        工艺齐套接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gidList': {'type': 'array'},
        #         'refType': ['10010', '10020']
        #     },
        #     'required': [
        #         'gidList',
        #         'refType'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeKittingManage/routLineKitting.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def kitting_material(self, data):
        """
        物料齐套接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gidList': {'type': 'array'},
        #         'refType': ['10010', '10020']
        #     },
        #     'required': [
        #         'gidList',
        #         'refType'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeKittingManage/materialKitting.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def kitting_qcStandard(self, data):
        """
        质检标准齐套接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gidList': {'type': 'array'},
        #         'refType': ['10010', '10020']
        #     },
        #     'required': [
        #         'gidList',
        #         'refType'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeKittingManage/qcStandardKitting.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def kitting_routeLineDoc(self, data):
        """
        工艺图文档齐套接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gidList': {'type': 'array'},
        #         'refType': ['10010', '10020']
        #     },
        #     'required': [
        #         'gidList',
        #         'refType'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeKittingManage/routeLineDocKitting.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def kitting_query(self, data):
        """
        齐套查询接口
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
        #                             'field': ['refCode'],
        #                             'type': ['like'],
        #                             'value': {'type': 'string'},
        #                             'operator': ['and']
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
        kwargs.setdefault('url', '/ime-container/imeKittingManage/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
