from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestForm():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("1061556745@qq.com")
        self.driver.find_element_by_id("user_password").send_keys("33sunshine")
        self.driver.find_element_by_id("user_remember_me").click()
        ele_submit = self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        action = ActionChains(self.driver)
        action.move_to_element(ele_submit)
        action.click(ele_submit)
        action.perform()

        sleep(5)
