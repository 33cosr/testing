import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome('C:\Jenny\Software\chromedriver\chromedriver.exe')
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(3)

    def test_wait2(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, 'su').click()
        # self.driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys("hello world")
        # self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("hello")
        # self.driver.find_element(By.ID,"kw").send_keys("hello python")

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()

        # time.sleep(3)

        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) < 1

        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]'))
        # WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH,
                                 '//*[@title="the most active topics in the last year, month, week or day"]').click()

        print('hello')
