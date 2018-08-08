# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import inspectbill_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class InspectBillDispatch(unittest.TestCase):
    u'''点检单派工'''
    def setUp(self):
        pass

    def test_inspectbill_dispatch_simple(self):
        u'''单个点检单派工'''
        # 获取点检单gid
        ibgids = []
        ibgid = inspectbill_public.inspectbill_create()
        ibgids.append(ibgid)
        inspectbill_public.inspectbill_dispatch(ibgids)
        sreq = inspectbill_public.inspectbill_select(ibgid)
        # print('===========', sreq)
        if 'status":"20' in sreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_inspectbill_dispatch_more(self):
        u'''点检单批量派工'''
        # 获取点检单gid
        ibgids = []
        for c in range(3):
            ibgid = inspectbill_public.inspectbill_create()
            ibgids.append(ibgid)
            inspectbill_public.inspectbill_dispatch(ibgids)
        check = 0
        for ibgid in ibgids:
            sreq = inspectbill_public.inspectbill_select(ibgid)
            # print('===========', sreq)
            if 'status":"20' in sreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    # def test_maintainbill_dispatch_again(self):
    #     u'''点检单多次派工'''
    #     # 获取保养单gid
    #     ibgids = []
    #     ibgid = inspectbill_public.inspectbill_create()
    #     ibgids.append(ibgid)
    #     inspectbill_public.inspectbill_dispatch(ibgids)
    #     dpreq = inspectbill_public.inspectbill_dispatch(ibgids)
    #     # print('===========', dpreq)
    #     if 'message":"只有已创建的点检单才能派工' in dpreq:
    #         assert 1 == 1
    #     else:
    #         assert 1 == 2

    # def test_maintainbill_dispatch_recorded(self):
    #     u'''已报工的点检单派工'''
    #     # 获取保养单gid
    #     pass


if __name__ == '__main__':
    unittest.main()
