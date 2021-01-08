import time

from selenium import webdriver


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Firefox(executable_path='C:\Jenny\Software\geckodriver\geckodriver.exe')
        self.driver.implicitly_wait(5) # 全局作用于所有的find_element 方法
    # 显示等待
    # WebDriverWait
    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("热门").click()
        # self.driver.find_element_by_link_text("").click()