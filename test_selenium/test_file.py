from time import sleep

from test_selenium.base import Base


class TestFile(Base):

    def test_file(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("C:\Jenny\Study\python\pytest_practice\\test_selenium\img\\baidu.png")
        sleep(3)
