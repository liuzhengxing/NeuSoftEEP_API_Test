# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import maintainbill_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class MaintainBillDispatch(unittest.TestCase):
    u'''保养单派工'''
    def setUp(self):
        pass

    def test_maintainbill_dispatch_simple(self):
        u'''单个保养单派工'''
        # 获取保养单gid
        mbgids = []
        mbgid = maintainbill_public.maintainbill_create()
        mbgids.append(mbgid)
        maintainbill_public.maintainbill_dispatch(mbgids)
        sreq = maintainbill_public.maintainbill_select(mbgid)
        # print('===========', sreq)
        if '"status":"20"' in sreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_maintainbill_dispatch_more(self):
        u'''保养单批量派工'''
        # 获取保养单gid
        mbgids = []
        for c in range(3):
            mbgid = maintainbill_public.maintainbill_create()
            mbgids.append(mbgid)
        maintainbill_public.maintainbill_dispatch(mbgids)
        check = 0
        for mbgid in mbgids:
            sreq = maintainbill_public.maintainbill_select(mbgid)
            # print('===========', sreq)
            if '"status":"20"' in sreq:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_maintainbill_dispatch_again(self):
        u'''保养单多次派工'''
        # 获取保养单gid
        mbgids = []
        mbgid = maintainbill_public.maintainbill_create()
        mbgids.append(mbgid)
        maintainbill_public.maintainbill_dispatch(mbgids)
        dpreq = maintainbill_public.maintainbill_dispatch(mbgids)
        # sreq = maintainbill_public.maintainbill_select(mbgid)
        # print('===========', dpreq)
        if 'message":"只有已创建的保养单才能派工' in dpreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_maintainbill_dispatch_recorded(self):
        u'''已报工的保养单派工'''
        # 获取保养单gid
        mbgids = []
        mbgid = maintainbill_public.maintainbill_create()
        mbgids.append(mbgid)
        maintainbill_public.maintainbill_dispatch(mbgids)
        maintainbill_public.maintainbill_saveorrecord(mbgid, 'record')
        mdreq = maintainbill_public.maintainbill_dispatch(mbgids)
        # print(mdreq)
        if 'message":"只有已创建的保养单才能派工' in mdreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
