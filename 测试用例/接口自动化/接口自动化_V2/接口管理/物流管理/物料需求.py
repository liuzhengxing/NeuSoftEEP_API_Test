# _*_ coding:utf-8 _*_

from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class MaterialRequirement:
    """
    物料需求类
    """
    def materialmrequirement_add(self, data):
        """
        直接创建物料需求
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogisticsMaterialRequirement/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def materialmrequirement_referenceGeneration(self, data):
        """
        工单转换成物料需求并保存接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogisticsMaterialRequirement/referenceGeneration.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def materialmrequirement_findById(self, data):
        """
        物料需求详情查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'GET')
        kwargs.setdefault('url', '/ime-container/imeLogisticsMaterialRequirement/findById.action?gid=' + data)
        req = nr(**kwargs)
        return req

    def materialmrequirement_getResourceCodeByGid(self, data):
        """
        来源单号查询接口
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/logistics/getResourceCodeByGid.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def materialmrequirement_queryByData(self, data):
        """
        按需查询物料需求
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogisticsMaterialRequirement/query.action?usedPost=true')
        kwargs.setdefault('data', data)
        kwargs.setdefault('dataSource', '43a917f8-3377-45d6-8d8e-c618feb9b5dc')
        req = nr(**kwargs)
        return req

    def materialmrequirement_manuallyWarehouse(self, data):
        """
        物料需求手工分配仓库
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogisticsMaterialRequirement/manuallyWarehouse.action?all=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def materialmrequirement_autoWarehouse(self, data):
        """
        物料需求按条件自动分配仓库
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogisticsMaterialRequirement/autoWarehouse.action?'
                                 'usedPost=true&all=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def materialmrequirement_autoWarehouseByGid(self, data):
        """
        指定物料需求自动分配仓库
        :param data:
        :return:
        """
        kwargs = {}

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeLogisticsMaterialRequirement/autoWarehouseByGid.action?all=true')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
