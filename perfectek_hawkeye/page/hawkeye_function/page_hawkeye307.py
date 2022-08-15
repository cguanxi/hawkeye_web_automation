from selenium.webdriver.common.by import By
from base.action_base import ActionBase


class HawkeyeCase(ActionBase):
    username = By.XPATH, '//*[@id="username"]'
    password = By.XPATH, '//*[@id="password"]'
    btn_login = By.XPATH, '//*[@id="btn-login"]'
    btn_add_testcase = By.XPATH, '//*[@id="btn-add-testcase"]'
    testcase_name = By.XPATH, '//*[@id="testcase-name"]'
    pdf_button = By.XPATH, '//*[@id="page-content"]/div[1]/div[2]/div/div[4]/div/div/label'
    add_crate = By.XPATH, '//*[@id="chassis-add"]'
    crate_type = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select'
    select_m2ua = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[8]'
    select_dwa16rf_wlpx = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[7]'
    select_dwa16rf_wlpc = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[6]'
    select_dwa16rf_rfc5 = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[5]'
    select_dna16c = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[4]'
    select_dea1016 = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[3]'
    select_dea6016 = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[2]'
    select_dba8000 = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[1]/select/option[1]'
    crate_name = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[2]/input'
    crate_ip = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[2]/div[3]/input'
    crate_ok = By.XPATH, '//*[@id="modal-addChassis"]/div/div/div[3]/button[1]'
    m2ua_the_editor1 = By.XPATH, '//*[@id="div-chassis"]/div/div/span[6]/i[3]'
    m2ua_the_editor2 = By.XPATH, '//*[@id="div-chassis"]/div/div/div[1]/span[6]/i[3]'
    m2ua_slot1 = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[1]/select'
    slot1_la1g20c = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[1]/select/option[1]'
    slot1_la10g16f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[1]/select/option[2]'
    slot1_la10g8f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[1]/select/option[3]'
    slot1_va4hdmi = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[1]/select/option[4]'
    slot1_va2h4k = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[1]/select/option[5]'
    m2ua_slot2 = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[2]/select'
    slot2_la1g20c = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[2]/select/option[1]'
    slot2_la10g16f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[2]/select/option[2]'
    slot2_la10g8f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[2]/select/option[3]'
    slot2_va4hdmi = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[2]/select/option[4]'
    slot2_va2h4k = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[2]/select/option[5]'
    m2ua_slot3 = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[3]/select'
    slot3_la1g20c = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[3]/select/option[1]'
    slot3_la10g16f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[3]/select/option[2]'
    slot3_la10g8f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[3]/select/option[3]'
    slot3_va4hdmi = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[3]/select/option[4]'
    slot3_va2h4k = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[3]/select/option[5]'
    m2ua_slot4 = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[4]/select'
    slot4_la1g20c = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[4]/select/option[1]'
    slot4_la10g16f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[4]/select/option[2]'
    slot4_la10g8f = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[4]/select/option[3]'
    slot4_va4hdmi = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[4]/select/option[4]'
    slot4_va2h4k = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[2]/div[4]/div[4]/select/option[5]'
    board_card_ok = By.XPATH, '//*[@id="modal-editChassis"]/div/div/div[3]/button[1]'
    update_m2ua_crate = By.XPATH, '//*[@id="div-chassis"]/div/div/div/span[6]/i[1]'
    update_m2ua_crate_ok = By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/button'

    # 账号密码登录
    def the_login(self, username: object, password: object):
        self.find_element_send_keys(HawkeyeCase.username, username)
        self.find_element_send_keys(HawkeyeCase.password, password)
        self.find_element_click(HawkeyeCase.btn_login)

    # 添加测试例输入测试例名
    def test_name(self, case_name: object):
        self.find_element_click(HawkeyeCase.btn_add_testcase)
        self.find_element_send_keys(HawkeyeCase.testcase_name, case_name)

    # PDF 开关
    def pdf_switch(self):
        self.find_element_click(HawkeyeCase.pdf_button)

    # 添加M2UA机箱
    def m2ua_crate(self, m2ua_name: object, m2ua_ip: object):
        self.find_element_click(HawkeyeCase.add_crate)
        self.find_element_click(HawkeyeCase.crate_type)
        self.find_element_click(HawkeyeCase.select_m2ua)
        self.find_element_send_keys(HawkeyeCase.crate_name, m2ua_name)
        self.find_element_send_keys(HawkeyeCase.crate_ip, m2ua_ip)
        self.find_element_click(HawkeyeCase.crate_ok)

    # 机箱编辑
    def the_editor1_m2ua(self):
        self.find_element_click(HawkeyeCase.m2ua_the_editor1)

    def the_editor2_m2ua(self):
        self.find_element_click(HawkeyeCase.m2ua_the_editor2)

    # 模块确定
    def the_editor_ok(self):
        self.find_element_click(HawkeyeCase.board_card_ok)

    # 四张1G流量卡选择
    def the_editor_la10g20c(self):
        self.find_element_click(HawkeyeCase.m2ua_slot1)
        self.find_element_click(HawkeyeCase.slot1_la1g20c)
        self.find_element_click(HawkeyeCase.m2ua_slot2)
        self.find_element_click(HawkeyeCase.slot2_la1g20c)
        self.find_element_click(HawkeyeCase.m2ua_slot3)
        self.find_element_click(HawkeyeCase.slot3_la1g20c)
        self.find_element_click(HawkeyeCase.m2ua_slot4)
        self.find_element_click(HawkeyeCase.slot4_la1g20c)

    # 四张10G16口流量卡选择
    def the_editor_la10g16f(self):
        self.find_element_click(HawkeyeCase.m2ua_slot1)
        self.find_element_click(HawkeyeCase.slot1_la10g16f)
        self.find_element_click(HawkeyeCase.m2ua_slot2)
        self.find_element_click(HawkeyeCase.slot2_la10g16f)
        self.find_element_click(HawkeyeCase.m2ua_slot3)
        self.find_element_click(HawkeyeCase.slot3_la10g16f)
        self.find_element_click(HawkeyeCase.m2ua_slot4)
        self.find_element_click(HawkeyeCase.slot4_la10g16f)

    # 四张10G8口流量卡选择
    def the_editor_la10g8f(self):
        self.find_element_click(HawkeyeCase.m2ua_slot1)
        self.find_element_click(HawkeyeCase.slot1_la10g8f)
        self.find_element_click(HawkeyeCase.m2ua_slot2)
        self.find_element_click(HawkeyeCase.slot2_la10g8f)
        self.find_element_click(HawkeyeCase.m2ua_slot3)
        self.find_element_click(HawkeyeCase.slot3_la10g8f)
        self.find_element_click(HawkeyeCase.m2ua_slot4)
        self.find_element_click(HawkeyeCase.slot4_la10g8f)

    # 四张四口HDMI卡选择
    def the_editor_va4hdmi(self):
        self.find_element_click(HawkeyeCase.m2ua_slot1)
        self.find_element_click(HawkeyeCase.slot1_va4hdmi)
        self.find_element_click(HawkeyeCase.m2ua_slot2)
        self.find_element_click(HawkeyeCase.slot2_va4hdmi)
        self.find_element_click(HawkeyeCase.m2ua_slot3)
        self.find_element_click(HawkeyeCase.slot3_va4hdmi)
        self.find_element_click(HawkeyeCase.m2ua_slot4)
        self.find_element_click(HawkeyeCase.slot4_va4hdmi)

    # 四张二口H4K卡选择
    def the_editor_va2h4k(self):
        self.find_element_click(HawkeyeCase.m2ua_slot1)
        self.find_element_click(HawkeyeCase.slot1_va2h4k)
        self.find_element_click(HawkeyeCase.m2ua_slot2)
        self.find_element_click(HawkeyeCase.slot2_va2h4k)
        self.find_element_click(HawkeyeCase.m2ua_slot3)
        self.find_element_click(HawkeyeCase.slot3_va2h4k)
        self.find_element_click(HawkeyeCase.m2ua_slot4)
        self.find_element_click(HawkeyeCase.slot4_va2h4k)

    # 更新机箱状态
    def m2ua_crate_update(self):
        self.find_element_click(HawkeyeCase.update_m2ua_crate)
        self.find_element_click(HawkeyeCase.update_m2ua_crate_ok)
