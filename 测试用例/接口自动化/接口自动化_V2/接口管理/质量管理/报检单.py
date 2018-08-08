# encoding: utf-8
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr

class QualityRecord():
    """报检单类"""



    def qualityRecord_add(self,data):
        "质检工单生成报检单，派检单生成报检单"

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityRecord/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req

    def reportRecord(self,data):
        """报检"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeQualityRecord/reportRecord.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req