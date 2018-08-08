# encoding: utf-8
from 测试用例.接口自动化.接口自动化_V2.接口测试.public_method import neu_reqeust as nr

class TrackQualityOrder():
    """派检单类"""

    def trackQualityOrder_add(self,data):
        """质检工单生成派检单"""

        kwargs = {}
        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imeTrackQualityOrder/add.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req