# _*_coding: utf-8 _*_

import unittest

from public import params

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class InspectBillModify(unittest.TestCase):
    def setUp(self):
        pass

    def test_inspectbill_modify(self):
        u'''点检单修改'''


    def test_inspectbill_modify_created(self):
        u'''已创建的点检单修改'''
        pass


    def test_inspectbill_modify_dispathed(self):
        u'''已派工的点检单修改'''
        pass


    def test_inspectbill_modify_reported(self):
        u'''已报工的点检单修改'''
        # 获取保养单gid
        pass
    

if __name__ == '__main__':
    unittest.main()
