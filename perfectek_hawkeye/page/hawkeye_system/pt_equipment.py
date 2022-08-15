from selenium.webdriver.common.by import By
from base.action_base import ActionBase


class PtEquipment(ActionBase):
    system = By.XPATH, '//*[@id="func-04"]/a'
    system_restart = By.XPATH, '//*[@id="func-0404"]/a'
    shut_down = By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div[2]/div/div/div/button'
    determine_button = By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/button'

    # 设备管理系统关机步骤
    def pt_equipment(self):
        self.find_element_click(PtEquipment.system)
        self.find_element_click(PtEquipment.system_restart)
        self.find_element_click(PtEquipment.shut_down)
        self.find_element_click(PtEquipment.determine_button)
