# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import maintainbill_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class MaintainBillSave(unittest.TestCase):
    u'''保养单保存'''
    def setUp(self):
        pass

    def test_maintainbill_save(self):
        u'''保养单报工'''
        # 获取保养单gid
        mbgids = []
        mbgid = maintainbill_public.maintainbill_create()
        mbgids.append(mbgid)
        # 保养单派工
        maintainbill_public.maintainbill_dispatch(mbgids)
        # 保养单报工
        maintainbill_public.maintainbill_saveorrecord(mbgid, 'save')
        sreq = maintainbill_public.maintainbill_select(mbgid)
        if '"status":"20"' in sreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
