import time

import pytest
from selenium.webdriver import ActionChains

from wrapper.BasePage import BasePage
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_001_Demo:
    baseURL = ReadConfig.getApplicationURL("baseURL")
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_001_enroll_course(self):
        self.logger.info("Test_001_enroll_course")
        self.logger.info("Started Enroll Course")
        self.driver.get(self.baseURL)
        self.homePage = HomePage(self.driver)
        self.basePage = BasePage(self.driver)
        self.homePage.click_enroll_a_course_button()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        time.sleep(30)
        self.homePage.click_enroll_first_course()
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_text_element_should_be_displayed('strong', 'Personal details')
        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutPage.set_first_name('Sandbox')
        self.checkoutPage.set_last_name('Axi Testing')
        self.checkoutPage.set_street_address('hanoi 123')
        self.checkoutPage.set_phone('+923265233')
        self.checkoutPage.set_email_address('binh.n@academyxi.com')
        self.checkoutPage.set_bod('15/06/1993')


