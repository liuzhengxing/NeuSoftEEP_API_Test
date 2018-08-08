import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import inspectbill_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class InspectBillSelect(unittest.TestCase):
    def setUp(self):
        pass

    def test_inspectbill_select_detail(self):
        u'''查询点检单详情'''
        # 生成点检单
        ibgid = inspectbill_public.inspectbill_create()
        # 查询点检单详情
        sreq = inspectbill_public.inspectbill_select(ibgid)
        if ibgid in sreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_inspectbill_select_list(self):
        u'''点检单列表查询'''
        freq = inspectbill_public.inspectbill_find('')
        if '"data":' in freq and '"success":true' in freq and '"pager":' in freq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_inspectbill_find_crosswise(self):
        u'''查询点检单详情子表信息'''
        # 生成点检单
        ibgid = inspectbill_public.inspectbill_create()
        freq = inspectbill_public.inspectbill_findCrosswiseById(ibgid)
        if 'mdInspectObjectGid' in freq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
