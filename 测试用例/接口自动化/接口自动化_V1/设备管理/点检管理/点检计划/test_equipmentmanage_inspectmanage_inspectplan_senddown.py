# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import equipmentmanage_public
from 测试用例.接口自动化.接口自动化_V1.设备管理 import inspectplan_public

domain = params.testdomain
port = params.testport

headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class InspectPlanSenddown(unittest.TestCase):
    u'''点检计划发布'''
    def setUp(self):
        pass

    def test_inspectplan_senddown_simple(self):
        u'''单个点检计划下发'''
        # 创建点检计划
        ipgids = []
        ipgid = inspectplan_public.inspectplan_create()
        ipgids.append(ipgid)

        # 关联设备
        equipmentmanage_public.associationequipment(ipgid)

        # 下发点检计划
        inspectplan_public.inspectplan_senddown(ipgids)

        # 验证下发
        sreq = inspectplan_public.inspectplan_select(ipgid)
        # print(sreq)
        if 'status":"20' in sreq:
            assert 1 == 1
        else:
            assert 1 == 2


    def test_inspectplan_senddown_noequment(self):
        u'''未关联设备的点检计划下发'''
        # 创建点检计划
        ipgids = []
        ipgid = inspectplan_public.inspectplan_create()
        ipgids.append(ipgids)

        # 下发点检计划
        sdreq = inspectplan_public.inspectplan_senddown(ipgids)
        # print('==========', sdreq)

        # 验证
        if 'message":"点检设备为空，请先维护点检设备！' in sdreq:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_inspectplan_senddown_uncreate(self):
        u'''非已创建状态的点检计划下发'''
        # 创建点检计划
        ipgids = []
        ipgid = inspectplan_public.inspectplan_create()
        ipgids.append(ipgid)

        # 关联设备
        equipmentmanage_public.associationequipment(ipgid)

        # 下发点检计划
        inspectplan_public.inspectplan_senddown(ipgids)

        # 已下发的点检计划再次下发
        sdreq = inspectplan_public.inspectplan_senddown(ipgids)
        # print(sdreq)

        # 验证下发
        if 'message":"已下发过的点检计划不能再次发布' in sdreq:
            assert 1 == 1
        else:
            assert 1 == 2


if __name__ == '__main__':
    unittest.main(0)
