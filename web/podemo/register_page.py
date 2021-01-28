from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    # register information
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.ID, 'corp_name').send_keys("corp name")
        self.driver.find_element(By.ID, 'manager_name').send_keys("manger name")
        self.driver.find_element(By.ID, 'register_tel').send_keys("189029302")
        self.driver.find_element(By.ID, 'submit_btn').click()
        return True

    def register_success(self):
        return True

    def register_fail(self):
        return True
