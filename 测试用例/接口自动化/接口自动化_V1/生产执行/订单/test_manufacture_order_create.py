# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import lcl_data_order
from 测试用例.接口自动化.接口自动化_V1.生产执行.订单.order_public import order_create

SheetName = 'OrderCreate'


class OrderCreate(unittest.TestCase):
    u"""订单创建接口"""
    def setUp(self):
        pass

    def test_order_create_true(self):
        """必填项正常验证"""
        data = lcl_data_order(SheetName, 2)
        req = order_create(data)
        print('必填项正常验证', req)
        # noinspection PyBroadException
        try:
            ordergid = json.loads(req)['data']
            if ordergid is not None:
                assert 1 == 1
            else:
                assert 1 == 2
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2

    # def test_order_create_code_repeat(self):
    #     """订单编码重复"""
    #     data = lcl_data_order(SheetName, 3)
    #     # noinspection PyBroadException
    #     try:
    #         order_create(data)
    #         req = order_create(data)
    #         print('订单编码重复', req)
    #         assert json.loads(req)['cause'] == '订单编码已存在!'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_code_none(self):
    #     """订单编码为空"""
    #     data = lcl_data_order(SheetName, 4)
    #     data['code'] = ''
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('订单编码为空', req)
    #         assert json.loads(req)['cause'] == '必填字段[code]为空'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_workCenterGid_err(self):
    #     """工作中心gid不存在"""
    #     data = lcl_data_order(SheetName, 5)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('工作中心gid不存在', req)
    #         assert json.loads(req)['cause'] == '必填字段[workCenterGid]不存在'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_workCenterGid_none(self):
    #     """工作中心为空"""
    #     data = lcl_data_order(SheetName, 6)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('工作中心为空', req)
    #         assert json.loads(req)['cause'] == '必填字段[workCenterGid]为空'
    #     except Exception:
    #         assert 1 == 2
    #
    # def test_order_create_orderType_err(self):
    #     """订单类型不存在"""
    #     data = lcl_data_order(SheetName, 7)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('订单类型不存在', req)
    #         assert json.loads(req)['cause'] == '必填字段[orderType]不存在'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_orderType_none(self):
    #     """订单类型为空"""
    #     data = lcl_data_order(SheetName, 8)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('订单类型为空', req)
    #         assert json.loads(req)['cause'] == '必填字段[orderType]为空'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_materialGid_err(self):
    #     """物料gid不存在"""
    #     data = lcl_data_order(SheetName, 9)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('物料gid不存在', req)
    #         assert json.loads(req)['cause'] == '没有找到产品基础档案数据'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_materialGid_none(self):
    #     """物料gid为空"""
    #     data = lcl_data_order(SheetName, 10)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('物料gid为空', req)
    #         assert json.loads(req)['cause'] == '必填字段[materialGid]为空'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_materialVersion_err(self):
    #     """物料版本err"""
    #     data = lcl_data_order(SheetName, 11)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('物料版本err', req)
    #         assert json.loads(req)['cause'] == '物料版本必须是数字'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_materialVersion_none(self):
    #     """物料版本为空"""
    #     data = lcl_data_order(SheetName, 12)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('物料版本为空', req)
    #         assert json.loads(req)['cause'] == '物料版本必须是数字'
    #     except Exception:
    #         assert 1 == 2
    #
    # def test_order_create_planBeginTime_err(self):
    #     """计划开始时间err"""
    #     data = lcl_data_order(SheetName, 13)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('计划开始时间err', req)
    #         assert json.loads(req)['cause'] == '计划开始时间格式错误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_planBeginTime_wrong(self):
    #     """计划开始时间大于计划结束时间"""
    #     data = lcl_data_order(SheetName, 14)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('计划开始时间大于计划结束时间', req)
    #         assert json.loads(req)['cause'] == '计划的开始时间必须小于结束时间'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_planBeginTime_none(self):
    #     """计划开始时间为空"""
    #     data = lcl_data_order(SheetName, 15)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('计划开始时间为空', req)
    #         assert json.loads(req)['cause'] == '必填字段[planBeginTime]为空'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_planEndTime_none(self):
    #     """计划结束时间为空"""
    #     data = lcl_data_order(SheetName, 16)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('计划结束时间为空', req)
    #         assert json.loads(req)['cause'] == '必填字段[planEndTime]为空'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_planQty_err(self):
    #     """计划数量错误"""
    #     data = lcl_data_order(SheetName, 17)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('计划数量错误', req)
    #         assert json.loads(req)['cause'] == '订单的计划数量不能小于0!'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_planQty_none(self):
    #     """计划数量为空"""
    #     data = lcl_data_order(SheetName, 18)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('计划数量为空', req)
    #         assert json.loads(req)['cause'] == '必填字段[planQty]为空'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_finishQty_err(self):
    #     """创建时包含已完工数量"""
    #     data = lcl_data_order(SheetName, 19)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('创建时包含已完工数量', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_finishQty_wrong(self):
    #     """完工数量大于计划数量"""
    #     data = lcl_data_order(SheetName, 20)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('完工数量大于计划数量', req)
    #         assert json.loads(req)['cause'] == '订单的计划数量不能小于完工数量'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_finishQty_wrong2(self):
    #     """完工数量为负数"""
    #     data = lcl_data_order(SheetName, 21)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('完工数量为负数', req)
    #         assert json.loads(req)['cause'] == '订单的完工数量不能小于0!'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_publishedQty_wrong(self):
    #     """下发数量大于计划数量"""
    #     data = lcl_data_order(SheetName, 22)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('下发数量大于计划数量', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_qualifiedQty_wrong(self):
    #     """合格数量大于计划数量"""
    #     data = lcl_data_order(SheetName, 23)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('合格数量大于计划数量', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_unqualifiedQty_wrong(self):
    #     """不合格数量大于计划数量"""
    #     data = lcl_data_order(SheetName, 24)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('不合格数量大于计划数量', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_wasteQty_wrong(self):
    #     """废品数量大于计划数量"""
    #     data = lcl_data_order(SheetName, 25)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('废品数量大于计划数量', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_orderStatus_wrong(self):
    #     """订单状态错误"""
    #     data = lcl_data_order(SheetName, 26)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('订单状态错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_planOrderSource_wrong(self):
    #     """来源订单不存在"""
    #     data = lcl_data_order(SheetName, 27)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('来源订单不存在', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_planOrderCategory_wrong(self):
    #     """订单类别错误"""
    #     data = lcl_data_order(SheetName, 28)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('订单类别错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_orderSeq_wrong(self):
    #     """订单顺序错误"""
    #     data = lcl_data_order(SheetName, 29)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('订单顺序错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_factoryLineGid_wrong(self):
    #     """产线错误"""
    #     data = lcl_data_order(SheetName, 30)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('产线错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_actualTime_wrong(self):
    #     """实际开始时间大于实际结束时间"""
    #     data = lcl_data_order(SheetName, 31)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('实际开始时间大于实际结束时间', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_measureTime_wrong(self):
    #     """测算开始时间大于测算结束时间"""
    #     data = lcl_data_order(SheetName, 32)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('测算开始时间大于测算结束时间', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_bomStatus_wrong(self):
    #     """BOM状态错误"""
    #     data = lcl_data_order(SheetName, 33)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('BOM状态错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create(self):
    #     """订单进程错误"""
    #     data = lcl_data_order(SheetName, 34)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('订单进程错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_canOperation_wrong(self):
    #     """是否可操作错误"""
    #     data = lcl_data_order(SheetName, 35)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('是否可操作错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2
    #
    # def test_order_create_surplusOrderFlag_wrong(self):
    #     """是否余量订单错误"""
    #     data = lcl_data_order(SheetName, 36)
    #     # noinspection PyBroadException
    #     try:
    #         req = order_create(data)
    #         print('是否余量订单错误', req)
    #         assert json.loads(req)['cause'] == '输入参数有误'
    #     except Exception as e:
    #         print('接口执行错误', e)
    #         assert 1 == 2


if __name__ == '__main__':
    unittest.main()
