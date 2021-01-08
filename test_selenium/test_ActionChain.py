from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ActionChains 只是针对PC端程序鼠标模拟的系列操作，对H5页面操作时无效
# TouchAction可以对h5页面操作。 实现点击 华东 拖拽 多点触控，以及模拟手势的各种操作

class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome('C:\Jenny\Software\chromedriver\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        element_double_click = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        element_right_click = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_right_click)
        action.double_click(element_double_click)
        action.perform()

    def test_movetoelement(self):
        self.driver.get('http://www.baidu.com')
        element = self.driver.find_element(By.XPATH, '//span[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element(By.XPATH, '//div[@id="dragger"]')
        drop_element = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element).perform()
        ## or 2
        # action.click_and_hold(drag_element).release(drop_element).perform()
        # or 3
        # action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

# 模拟键盘操作
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        action = ActionChains(self.driver)
        action.click(ele)
        action.send_keys("jenny").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("hello").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

    #TouchAction

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_ActionChain.py'])
