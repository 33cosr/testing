from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def addmember(self, username, account, phonenum):
        # sleep(2)
        self.find(By.ID, 'username').send_keys(username)
        # self.driver.find_element(By.ID, 'memberAdd_english_name').send_keys('jennylov')
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        self.find(By.ID, 'memberAdd_phone').send_keys(phonenum)
        # self.driver.find_element(By.ID, 'memberAdd_telephone').send_keys("2839482")
        # # self.driver.find_element(By.ID, 'memberAdd_mail').send_keys("238948322@qq.com")
        # self.driver.find_element(By.ID, 'memberEdit_address').send_keys("nanjing")
        # self.driver.find_element(By.ID, 'memberAdd_title').send_keys("manager")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # checkbox 加载成功 可点击
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)

        # sleep()
        return True

    def get_member(self,value):
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr>:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            if value in titlelist:
                return True
            total_list = total_list + titlelist
            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split("/", 1)
            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return total_list
