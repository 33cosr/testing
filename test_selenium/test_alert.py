from time import sleep

from selenium.webdriver import ActionChains

from test_selenium.base import Base


class TestAlert(Base):

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        ele_drag = self.driver.find_element_by_id("draggable")
        ele_drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop)
        action.perform()
        sleep(3)
        self.driver.switch_to.alert.accept()
        print("click alert")
        self.driver.switch_to.default_content()

        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
