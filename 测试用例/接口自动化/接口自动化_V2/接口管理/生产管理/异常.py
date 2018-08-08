# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class Anomaly:
    """
    异常类
    """

    def anomalytype_create(self, data):
        """
        异常类型创建接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'code': {'type': 'string'},
        #         'name': {'type': 'string'},
        #         'category': {'type': 'string'},
        #         'description': {'type': 'string'},
        #         'responseRoleGid': {'type': 'string'},
        #         'handleRoleGid': {'type': 'string'}
        #     },
        #     'required': [
        #         'code',
        #         'name'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomalyType/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalytype_modify(self, data):
        """
        异常类型更新接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gid': {'type': 'string'},
        #         'code': {'type': 'string'},
        #         'name': {'type': 'string'},
        #         'category': {'type': 'string'},
        #         'description': {'type': 'string'},
        #         'responseRoleGid': {'type': 'string'},
        #         'handleRoleGid': {'type': 'string'}
        #     },
        #     'required': [
        #         'gid',
        #         'code',
        #         'name'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomalyType/modify.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalytype_delete(self, data):
        """
        异常类型删除接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomalyType/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalytype_query(self, data):
        """
        异常类型查询接口
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
        #                             'field': ['code'],
        #                             'type': ['like'],
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
        kwargs.setdefault('url', '/ime-container/imeAnomalyType/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalytype_findById(self, data):
        """
        异常类型详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeAnomalyType/findById.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def anomaly_add(self, data):
        """
        异常对象创建接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'code': {'type': 'string'},
        #         'state': {'type': 'string'},
        #         'category': {'type': 'string'},
        #         'typeGid': {'type': 'string'},
        #         'anomalyLevel': {'type': 'string'},
        #         'reason': {'type': 'string'},
        #         'sourceType': {'type': 'string'},
        #         'sourceGid': {'type': 'string'},
        #         'sourceCode': {'type': 'string'},
        #         'toucherGid': {'type': 'string'},
        #         'touchTime': {'type': 'string'},
        #         'stationCode': {'type': 'string'},
        #         'stationName': {'type': 'string'},
        #         'responseRoleGid': {'type': 'string'}
        #     },
        #     'required': [
        #         'code'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomaly/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomaly_modify(self, data):
        """
        异常对象更新接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'gid': {'type': 'string'},
        #         'code': {'type': 'string'},
        #         'state': {'type': 'string'},
        #         'category': {'type': 'string'},
        #         'typeGid': {'type': 'string'},
        #         'anomalyLevel': {'type': 'string'},
        #         'reason': {'type': 'string'},
        #         'sourceType': {'type': 'string'},
        #         'sourceGid': {'type': 'string'},
        #         'sourceCode': {'type': 'string'},
        #         'toucherGid': {'type': 'string'},
        #         'touchTime': {'type': 'string'},
        #         'stationCode': {'type': 'string'},
        #         'stationName': {'type': 'string'},
        #         'responseRoleGid': {'type': 'string'}
        #     },
        #     'required': [
        #         'gid',
        #         'code'
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomaly/modify.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomaly_delete(self, data):
        """
        异常对象删除接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomaly/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomaly_query(self, data):
        """
        异常对象查询接口
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
        #                             'field': ['code'],
        #                             'type': ['like'],
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
        kwargs.setdefault('url', '/ime-container/imeAnomaly/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomaly_findById(self, data):
        """
        异常对象详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeAnomaly/findById.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def anomalyresponse_add(self, data):
        """
        异常响应创建接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'anomalyGid': {'type': 'string'},
        #         'handleRoleGid': {'type': 'string'},
        #         'receive': {'type': 'string'},
        #         'responderType': {'type': 'string'},
        #         'responseUserGid': {'type': 'string'},
        #         'suggest': {'type': 'string'},
        #         'remarks': {'type': 'string'}
        #     },
        #     'required': [
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomalyResponse/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalyresponse_query(self, data):
        """
        异常响应查询接口
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
        #                             'field': ['anomalyGid'],
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
        kwargs.setdefault('url', '/ime-container/imeAnomalyResponse/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalyresponse_findById(self, data):
        """
        异常响应详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomalyResponse/findById.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def anomalyhandle_add(self, gid, data):
        """
        异常处置创建接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'anomalyGid': {'type': 'string'},
        #         'result': {'type': 'string'},
        #         'receive': {'type': 'integer'},
        #         'handleType': {'type': 'string'},
        #         'nextHandleUserGid': {'type': 'string'},
        #         'handleUserGid': {'type': 'string'},
        #         'manner': {'type': 'string'},
        #         'remarks': {'type': 'string'}
        #     },
        #     'required': [
        #     ]
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomalyHandle/add.action?typeGid=' + gid)
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalyhandle_query(self, data):
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
        #                             'field': ['anomalyGid'],
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
        kwargs.setdefault('url', '/ime-container/imeAnomalyHandle/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def anomalyhandle_findById(self, data):
        """
        异常处置详情查询接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'string'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeAnomalyHandle/findById.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def anomaly_close(self, data):
        """
        异常对象关闭接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'array'
        # }
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeAnomaly/close.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
