import selenium
from selenium import webdriver

def test_case1():
    driver = webdriver.Chrome('C:\Jenny\Software\chromedriver\chromedriver.exe')
    driver.get("http://www.baidu.com")
