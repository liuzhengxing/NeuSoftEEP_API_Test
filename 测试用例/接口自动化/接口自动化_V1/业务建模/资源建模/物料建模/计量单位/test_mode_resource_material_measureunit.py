# _*_coding:utf-8_*_

import unittest

from public import params
from 测试用例.接口自动化.接口自动化_V1 import measureunit_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class MeasureUnit(unittest.TestCase):
    def setUp(self):
        pass

    def test_measureunit_create(self):
        u'''创建设备分类'''
        eccreq = measureunit_public.measureunit_create()
        if 'data":"' in eccreq and 'success":true' in eccreq:
            assert 1 == 1
        else:
            assert 1 == 2
