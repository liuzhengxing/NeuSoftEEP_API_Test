# _*_ coding:utf-8 _*_

from jsonschema import validate

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class ReportOrder:
    """
    报工类
    """

    def reportorder_report(self, data):
        """
        报工接口
        :param data:
        :return:
        """
        kwargs = {}
        # schema = {
        #     'type': 'object',
        #     'properties': {
        #         'reportOrderId': {'type': 'string'},
        #         'resourceOrderType': ['10020', '10030'],
        #         'imeReportOrderOperations': {
        #             'type': 'array',
        #             'items': {
        #                 "type": "object",
        #                 'properties': {
        #                     'operationGid': {'type': 'string'},
        #                     'curQualifiedQty': {'type': 'number'},
        #                     'curRepairQty': {'type': 'number'},
        #                 },
        #                 'required': [
        #                     'operationId'
        #                 ]
        #             }
        #         },
        #     },
        #     'required': [
        #         'reportOrderId',
        #         'resourceOrderType'
        #     ]
        # }
        #
        # validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeReportOrder/report.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
