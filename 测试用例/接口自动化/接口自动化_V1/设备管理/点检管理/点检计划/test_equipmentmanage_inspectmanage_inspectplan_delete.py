# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1.设备管理 import inspectplan_public

domain = params.testdomain
port = params.testport
headers = {
            'Content-Tpye': 'application/json;charset=utf-8'
        }


class InspectPlanDelete(unittest.TestCase):
    u'''点检计划删除'''
    def setUp(self):
        pass

    def test_inspectplan_delete_simple(self):
        u'''单个删除点检计划'''
        # 创建点检计划
        ipgids = []
        ipgid = inspectplan_public.inspectplan_create()
        # print('============', gid)
        ipgids.append(ipgid)
        # 单个删除点检计划
        inspectplan_public.inspectplan_delete(ipgids)
        # 验证删除
        req = inspectplan_public.inspectplan_select(ipgid)
        # print(req)
        if ipgid not in req:
            assert 1 == 1
        else:
            assert 1 == 2

    def test_inspectplan_delete_more(self):
        u'''批量删除点检计划'''
        # 创建点检计划
        ipgids = []
        for c in range(3):
            gid = inspectplan_public.inspectplan_create()
            # print('============', gid)
            ipgids.append(gid)
        # print(ipgids)

        # 批量删除点检计划
        inspectplan_public.inspectplan_delete(ipgids)

        # 验证删除
        check = 0
        for ipgid in ipgids:
            req = inspectplan_public.inspectplan_select(ipgid)
            # print(req)
            if ipgid not in req:
                check = check + 0
            else:
                check = check + 1
        if check == 0:
            assert 1 == 1
        else:
            assert 1 == 2

    # def test_inspectplan_delete_uncreate(self):
    #     u'''删除非已创建状态的点检计划'''
    #     # 创建点检计划
    #     ipgids = []
    #     ipgid = inspectplan_public.inspectplan_create()
    #     ipgids.append(ipgid)
    #
    #     # 关联设备
    #     equipmentmanage_public.associationequipment(ipgid)
    #
    #     # 下发
    #     inspectplan_public.inspectplan_senddown(ipgids)
    #
    #     # 删除点检计划
    #     ipd = inspectplan_public.inspectplan_delete(ipgids)
    #     # print(ipd)


if __name__ == '__main__':
    unittest.main(0)
