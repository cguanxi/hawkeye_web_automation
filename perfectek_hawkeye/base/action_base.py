from selenium.webdriver.support.wait import WebDriverWait


class ActionBase:
    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def find_element(self, args, time=10, poll=1):
        # *args 设置默认不定长参数
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(*args))

    # 点击
    def find_element_click(self, args, time=10, poll=1):
        self.find_element(args, time, poll).click()

    # 输入
    def find_element_send_keys(self, args, text, time=10, poll=1):
        self.find_element(args, time, poll).send_keys(text)

    # 清除
    def find_element_clear(self, args, time=10, poll=1):
        self.find_element(args, time, poll).clear()

    # # 获取文本
    # def find_element_gettext(self, args, time=10, poll=1):
    #     return self.find_element(args, time, poll).text
