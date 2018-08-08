# _*_ coding:utf-8 _*_

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class InspectStrategy:
    """
    点检策略类
    """

    def inspectstrategiy_addBatch(self, data):
        """
        点检策略批量创建接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectStrategy/addBatch.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspectstrategiy_modify(self, data):
        """
        点检策略更新接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectStrategy/modify.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspectstrategiy_delete(self, data):
        """
        点检策略删除接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectStrategy/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspectstrategiy_query(self, data):
        """
        点检策略查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectStrategy/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspectstrategiy_findById(self, data):
        """
        点检策略详情查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeInspectStrategy/findById.action?gid={gid}'.format(gid=data))
        req = nr(**kwargs)
        return req

