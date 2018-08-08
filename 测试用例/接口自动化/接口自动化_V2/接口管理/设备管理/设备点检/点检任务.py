# _*_ coding:utf-8 _*_

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class InspectTask:
    """
    点检任务类
    """

    def inspecttask_addFromInspectStrategy(self, data):
        """
        根据策略批量创建点检任务接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/addFromInspectStrategy.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_addAndTrackFromInspectStrategy(self, data):
        """
        根据策略批量创建点检任务并派工接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/addAndTrackFromInspectStrategy.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_add(self, data):
        """
        点检任务创建接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_addAndTrack(self, data):
        """
        点检任务创建并派工接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/addAndTrack.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_track(self, data):
        """
        点检任务批量派工接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/track.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_report(self, data):
        """
        点检任务报工接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/report.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_modify(self, data):
        """
        点检任务更新接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/modify.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_delete(self, data):
        """
        点检任务删除接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_query(self, data):
        """
        点检任务查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def inspecttask_findById(self, data):
        """
        点检任务详情查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeInspectTask/findById.action?gid={gid}'.format(gid=data))
        req = nr(**kwargs)
        return req
