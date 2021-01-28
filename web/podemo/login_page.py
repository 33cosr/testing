from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        pass

    # go to register page
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()

        return RegisterPage(self.driver)
