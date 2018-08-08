# encoding: utf-8
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr


class QualityCollectList:
    """质量采集清单类"""

    def qualityCollectList_query(self, refGid, refType):
        """根据来源查询检测指标"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCollectList/queryCollectionListInfo.action?'
                                 'refGid=' + refGid + '&refType=' + str(refType))
        req = nr(**kwargs)
        return req

    def qualityCollectList_addBatch(self, data):
        """质检采集清单批量创建"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityCollectList/addBatch.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req
