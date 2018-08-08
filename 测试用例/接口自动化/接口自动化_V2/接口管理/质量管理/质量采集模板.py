# encoding: utf-8
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class QualityCollectTemplate():
    """质量采集模板类"""

    def saveQualityCollectTemplate(self, data):
        """保存采集模板"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCollectTemplate/saveQualityCollectTemplate.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def saveIndexType(self,data,gid):
        """保存指标分类"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeIndexType/saveIndexType.action?templateGid=' + str(gid))
        kwargs.setdefault('data',data)
        req = nr(**kwargs)
        return req

    def saveIndexValue(self,data):
        """保存指标"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeIndexValue/saveIndexValue.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def queryCollectTemplateIndex(self,refGid,refType):
        """来源查询采集模板（指标及选项）"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCollectTemplate/queryCollectTemplateIndex.action?usedPost=true&refGid=' + refGid + '&refType=' + refType)
        req = nr(**kwargs)
        return req

    def queryIndexTypeTree(self,templateGid):
        """通过模板查询分类树"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url','/ime-container/imeIndexType/queryIndexTypeTree.action?templateGid=' + str(templateGid))
        req = nr(**kwargs)
        return req

    def deleteQualityCollectTemplate(self, data):
        """删除采集模板"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCollectTemplate/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def deleteIndexType(self, data):
        """删除指标分类"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeIndexType/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def deleteIndexValue(self, data):
        """删除指标"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeIndexValue/delete.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
