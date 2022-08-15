import unittest
from time import sleep
from selenium import webdriver
from page.hawkeye_system.pt_equipment import PtEquipment


class TestEquipment(unittest.TestCase):
    # @unittest.skip 无条件忽略此用例
    @unittest.skip
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.equipment_script = PtEquipment(self.driver)

    def tearDown(self):
        sleep(3)
        self.driver.close()

    def test_equipment(self):
        # 隐式等待
        self.driver.implicitly_wait(3)
        # 关闭1.166机箱
        self.driver.get("http://172.16.1.166/cmn/page/appliance/list")
        self.equipment_script.pt_equipment()
        sleep(2)
        # 关闭1.113机箱
        self.driver.get("http://172.16.1.113/cmn/page/appliance/list")
        self.equipment_script.pt_equipment()
        print("---两台机箱已关机---")
