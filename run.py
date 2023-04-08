import unittest
from XTestRunner import HTMLTestRunner
from unittestreport import TestRunner

suite=unittest.TestLoader().discover("./","Test_Api.py")
with(open('./reports/result.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='Email 接口测试报告',
            description=["类型:api","地址**","字段：***"],
            language='zh-CN',
            tester='xxxx',
            verbosity=3
        )
        runner.run(
            testlist=suite,
            rerun=0,
            save_last_run=False
        )