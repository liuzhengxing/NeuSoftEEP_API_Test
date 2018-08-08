# encoding: utf-8
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr

class QualityWorkOrder():
    """质检工单类"""

    # def workOrder_Create(self,data):
    #     """工单创建，带业务单元"""
    #
    #     kwargs = {}
    #     kwargs.setdefault('method', 'POST')
    #     kwargs.setdefault('url', '/ime-container/imeWorkOrder/insertWorkOrder.action')
    #     kwargs.setdefault('data', data)
    #     req = nr(**kwargs)
    #     return req
    #
    # def workorder_changeStatut(self, data):
    #     """
    #     下发工单接口
    #     :param data:
    #     :return:
    #     """
    #     kwargs = {}
    #     # schema = {
    #     #     'type': 'array'
    #     # }
    #     # validate(data, schema)
    #
    #     kwargs.setdefault('method', 'POST')
    #     kwargs.setdefault('url', '/ime-container/imeWorkOrder/releaseWorkOrderChangeStatut.action')
    #     kwargs.setdefault('data', data)
    #     req = nr(**kwargs)
    #     return req

    def qualityWorkOrder_ref(self,data):
        """质检工单参照生成"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCheckOrder/refCreate.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def qualityWorkOrder_create(self,data):
        """质检工单直接创建"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCheckOrder/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def qualityWorkOrder_delete(self, data):
        """质检工单删除"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCheckOrder/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def qualityWorkOrder_rule(self,data):
        """质检工单下发规则修改"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQcRuleInfo/modify.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def qualityWorkOrder_query(self, data):
        """质检工单查询"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQcQac/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
