import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("scripts")
    hawkeye_case = open("自动化测试报告.html", "wb")
    HTMLTestRunner(hawkeye_case).run(suite)
