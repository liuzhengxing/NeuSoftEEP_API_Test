# _*_ coding:utf-8 _*_

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class LogBillReport:
    """
    物流报工类
    """

    def logbillreport_createByTrackBill(self, data):
        """
        物流单转换物流单报工单并保存接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogBillReport/createByTrackBill.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def logbillreport_reportByBill(self, data):
        """
        物流单报工-整单完工接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogBillReport/reportByBill.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def logbillreport_reportByBillDetail(self, data):
        """
        物流单报工-明细报工接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogBillReport/reportByBillDetail.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def logbillreport_queryByLogOperation(self, data):
        """
        物流单报工详情查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '//ime-container/imeLogBillReport/findById.action?gid={gid}'.format(gid=data))
        req = nr(**kwargs)
        return req

    def logbillreport_queryByData(self, data):
        """
        列表查询
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogBillReport/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        kwargs.setdefault('dataSource', 'f461351a-3bf7-4c5b-a6b2-336fe9cbaa2a')
        req = nr(**kwargs)
        return req