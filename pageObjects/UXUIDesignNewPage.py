import time

from selenium.webdriver import ActionChains

from wrapper.BasePage import BasePage


class UXUIDesignNewPage(BasePage):
    enrol_button = "//div[@class='course-infor course-enrol']//a[contains(@class, 'btn-addtocart')]"

    def __init__(self, driver):
        self.driver = driver

    def click_enrol_now_button(self, num):
        self.double_click(self.enrol_button)
        self.wait_for_loading_icon_disappear()
        if self.is_present(self.enrol_button):
           self.double_click(self.enrol_button)


