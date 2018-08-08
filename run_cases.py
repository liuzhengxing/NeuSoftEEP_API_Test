# -*- coding: utf-8 -*-

import time
import unittest

from pathlib import Path

from public.send_mail import send_email
from public import HTMLTestRunnerCN

# 执行测试
BaseDir = Path.cwd()

CaseDirs = []
CaseDir1 = BaseDir / '测试用例' / '接口自动化' / '接口自动化_V2' / '冒烟测试'
CaseDir2 = BaseDir / '测试用例' / '接口自动化' / '接口自动化_V2' / '接口测试'
CaseDirs.append(CaseDir1)

testunit = unittest.TestSuite()

# discover 方法定义
for CaseDir in CaseDirs:
    discover = unittest.defaultTestLoader.discover(start_dir=CaseDir, pattern='test*.py',
                                                   top_level_dir=BaseDir)

    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            print("cases：", test_case)
            testunit.addTests(test_case)
# 取前面时间
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
title = 'IME接口测试报告' + '_' + now
# 把当前时间加到报告中

if (BaseDir / 'report').exists() is False:
    (BaseDir / 'report').mkdir()
filepath = BaseDir / 'report' / (title + '.html')
print("testReport：", filepath)
fp = Path.open(filepath, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=title, description=u'用例执行情况：')

# 执行测试用例
runner.run(testunit)
time.sleep(3)

# 发送邮件
send_email(title, filepath)
