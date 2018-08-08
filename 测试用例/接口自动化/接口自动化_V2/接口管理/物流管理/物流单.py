# _*_ coding:utf-8 _*_

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class Logistics:
    """
    物流单类
    """

    def logistics_referenceGeneration(self, data):
        """
        物料需求转换成物流单并保存接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogTrackBill/referenceGeneration.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def logistics_bindLogRoute(self, data):
        """
        设置物流工艺模板接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogTrackBill/bindLogRoute.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def logistics_findById(self, data):
        """
        物流单详情查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeLogTrackBill/findById.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def logistics_queryByLogOperation(self, ids, sids):
        """
        根据工序查询物流单接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogTrackBill/queryByLogOperation.action?usedPost=true&'
                                 'ids={ids}&sids={sids}'.format(ids=ids, sids=sids))
        data = {
            "pager": {
                "page": 1,
                "pageSize": 10
            }
        }
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def logistics_queryByData(self, data):
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogTrackBill/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        kwargs.setdefault('dataSource', '73edd627-d8e7-4f98-9a3e-f1cf8f2e09cc')
        req = nr(**kwargs)
        return req
