# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestsuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome('C:\Jenny\Software\chromedriver\chromedriver.exe')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_simple(self):
        self.driver.get("https://www.baidu.com/")


    def test_testclickclose(self):
        self.driver.get("https://www.baidu.com/")
        # time.sleep(2)
        self.driver.set_window_size(875, 538)
        self.driver.find_element(By.CSS_SELECTOR, ".s-menu-item:nth-child(3)").click()
        self.driver.close()

    def test_testsearch(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(875, 538)
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("hello")
        self.driver.find_element(By.ID, "su").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.close()
