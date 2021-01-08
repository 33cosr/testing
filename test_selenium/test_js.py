import time

from selenium.webdriver.common.by import By

from test_selenium.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # return keyword
        ele = self.driver.execute_script('return document.getElementById("su")')
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        ele_nextpage = self.driver.find_element(By.XPATH, '// *[ @ id = "page"] / div / a[10]')
        ele_nextpage.click()
        time.sleep(3)
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        # document.getElementById("train_date")
        # a.removeAttribute("readonly")
        # a.value("2021-12-13")

        self.driver.get("https://www.12306.cn/index/")
        ele = self.driver.execute_script(
            'a = document.getElementById("train_date");a.removeAttribute("readonly");document.getElementById("train_date").value = "2021-03-04"')
        # self.driver.execute_script('document.getElementById("train_date").value = "2021-03-03"')
        print(ele)
        time.sleep(5)
