import unittest
from time import sleep
from selenium import webdriver
from page.hawkeye_function.page_hawkeye307 import HawkeyeCase


class TestHawkeye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.hawkeye_step = HawkeyeCase(self.driver)

    def tearDown(self):
        sleep(3)
        self.driver.close()

    def test_script(self):
        # 隐式等待
        self.driver.implicitly_wait(10)
        self.driver.get("http://172.16.100.106:8080/cmn/page/testcase/list")
        self.hawkeye_step.the_login("root", "root")
        self.hawkeye_step.test_name("web自动化")
        self.hawkeye_step.pdf_switch()
        self.hawkeye_step.m2ua_crate("M2UA", "172.16.100.106")
        sleep(1)
        self.hawkeye_step.the_editor1_m2ua()
        self.hawkeye_step.the_editor_la10g20c()
        self.hawkeye_step.the_editor_ok()
        sleep(2)
        self.hawkeye_step.the_editor2_m2ua()
        self.hawkeye_step.the_editor_la10g16f()
        self.hawkeye_step.the_editor_ok()
        sleep(2)
        self.hawkeye_step.the_editor2_m2ua()
        self.hawkeye_step.the_editor_la10g8f()
        self.hawkeye_step.the_editor_ok()
        sleep(2)
        self.hawkeye_step.the_editor2_m2ua()
        self.hawkeye_step.the_editor_va4hdmi()
        self.hawkeye_step.the_editor_ok()
        sleep(2)
        self.hawkeye_step.the_editor2_m2ua()
        self.hawkeye_step.the_editor_va2h4k()
        self.hawkeye_step.the_editor_ok()
        sleep(2)
        self.hawkeye_step.m2ua_crate_update()
