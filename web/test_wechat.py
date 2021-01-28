import shelve
from time import sleep

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 复用浏览器

# chrome --remote-debugging-port=9222
class TestWechat():

    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # sleep(3)
        # self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)

    def test_shelve(self):
        # 1 获取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        # print(cookies)

        # 2 打开
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 3 填入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 4 打开
        self.driver.refresh()
        sleep(3)

        # 5 找到元素 点击
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        sleep(2)
        # self.driver.find_element_by_id("js_upload_file_input").send_keys()

        # 6 发送文件 绝对路径
        self.driver.find_element_by_css_selector(".import_settingStage_upload_inputWrap input").send_keys(
            "C:\Jenny\\test world hello.xlsx")

        # 7 获取上传文件名
        filename = self.driver.find_element_by_id("upload_file_name").text
        print(filename)
        assert "test world hello.xlsx" == filename
        sleep(10)

    def test_cookie(self):
        # cookies = self.driver.get_cookies() # 当前打开页面的cookie
        cookies = [
            {'domain': '.qq.com', 'expiry': 1610168066, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2082138846.1610081199'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'V1_6_KtUSYO78uFrT_ovfRHwNEh8U17A7gsIJvwio1mL7EWMhJzona9jDx-ZknYz'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4684219'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850140013245'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3826084864'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '6561048269'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325094250438'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1612673754, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1673153666, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.457789762.1610081199'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1610112733, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '745ngbe'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1641541762, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1610081286'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '11734229602798360'},
            {'domain': '.qq.com', 'expiry': 1824268806, 'httpOnly': False, 'name': 'pt_sms_phone', 'path': '/',
             'secure': False, 'value': '138******98'},
            {'domain': '.qq.com', 'expiry': 1612522575, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '1061556745'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850140013245'},
            {'domain': '.qq.com', 'expiry': 1909471514, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False,
             'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'wH6VwV6bDHlDEd_iHELi8duFOaA9voh80fXLLvKbQ3dZbSs995GRMJVVg6Jtu0UPuNwKXjsueMI__WLWR1V5OUOuszSldpVGxEYenr9BwBi5sVX1PSCq8mwbLnXnl7dc8bCskzVlWgruU1iGBH6UmufOqWfZdsvQlSKGO0nYKW-HbBnrDEoGznUKYaBeoFgbKMLFNCxoLe5F74uBH4dRq2f3c6vQbOSJigwjed3o-tMeTsO7UsVr8FVDBieyp2PYN87JrM3Bh0kMWI69o126Pw'},
            {'domain': '.qq.com', 'expiry': 1890354145, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5de080e0310a1'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1641617285, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1610081215'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'uPZRdNBGUH'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '3c5ead7ad89440de8c558ee76f6ea72b6f138fa4498d25b9995145e8cfb84fb3'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.refresh()
