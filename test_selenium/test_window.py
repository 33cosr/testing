from time import sleep

from selenium import webdriver

from test_selenium.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("33sunshine")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13813007898")
        # switch login and click 用户名登陆
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("33sunshine")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("33sunshinejenny")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)
