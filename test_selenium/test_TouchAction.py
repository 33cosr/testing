from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

### issue
class TestTouchAction():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        pass

    def test_touchaction_scro(self):
        """
        open url http://www.baidu.com
        :return:
        """
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        ele_search.click()
        # action.perform()
        # action1.perform()

        # action.scroll_from_element(ele, 0, 10000).perform()
        # sleep(3)
