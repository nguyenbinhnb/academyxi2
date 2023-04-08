import time

import pytest
from selenium.webdriver import ActionChains

from pageObjects.BlogPage import BlogPage
from pageObjects.BuyNowPage import BuyNowPage
from pageObjects.CoursePage import CoursePage
from pageObjects.ElevateSelfPacedPage import ElevateSelfPacedPage
from pageObjects.HomePage import HomePage
from pageObjects.LandingPage import LandingPage
from pageObjects.OnlineCoursesPage import OnlineCoursesPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class Test_001_Frequent_Failures:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL("baseURL")
    onlineCoursesPageURL= ReadConfig.getApplicationURL("Online Courses Page")
    allCoursesListingURL = ReadConfig.getApplicationURL("All Courses Listing Page")
    customerExperienceDisciplineURL = ReadConfig.getApplicationURL("Customer Experience Discipline Page")
    buyNowURL = ReadConfig.getApplicationURL("Buy Now Page")
    lpSoftwareEngineerOnlineURL = ReadConfig.getApplicationURL("LP Software Engineer Online Page")
    lpUXUIOnlineURL = ReadConfig.getApplicationURL("LP UX UI Online Page")
    cxSelfPacedElevateURL = ReadConfig.getApplicationURL("CX Self Paced Elevate Page")
    blogsURL = ReadConfig.getApplicationURL("Blogs Page")

    # @pytest.mark.sanity
    @pytest.mark.smoke
    # @pytest.mark.regression
    def test_001_frequent_failures_on_home_page(self):
        self.logger.info("Test_001_frequent_failures_on_home_page")
        self.logger.info("Started Go To Home page")
        self.driver.get(self.baseURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        self.basePage.verify_broken_images()
    #
    @pytest.mark.smoke
    # @pytest.mark.regression
    def test_002_frequent_failures_on_blog_page(self):
        self.logger.info("Test_002_frequent_failures_on_blog_page")
        self.logger.info("Started Go To Blog page")
        self.driver.get(self.blogsURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        self.blogPage = BlogPage(self.driver)
        self.blogPage.verify_articles_amount()

    @pytest.mark.smoke
    # @pytest.mark.regression
    def test_003_frequent_failures_on_online_courses_page(self):
        self.logger.info("Test_003_frequent_failures_on_online_courses_page")
        self.logger.info("Started Go To Online Courses page")
        self.driver.get(self.allCoursesListingURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        self.basePage.verify_broken_images()

    @pytest.mark.smoke
    # @pytest.mark.regression
    def test_004_frequent_failures_on_courses_page(self):
        self.logger.info("Test_003_frequent_failures_on_online_courses_page")
        self.logger.info("Verify broken images on Customer Experience: Discipline page")
        self.basePage = BasePage(self.driver)
        self.driver.get(self.customerExperienceDisciplineURL)
        self.basePage.wait_for_page_load()
        self.basePage.verify_broken_images()
        self.logger.info("Verify broken images on Customer Experience: Elevate (Self-paced) page")
        self.driver.get(self.cxSelfPacedElevateURL)
        self.basePage.wait_for_page_load()
        self.basePage.verify_broken_images()

    @pytest.mark.smoke
    # @pytest.mark.regression
    def test_005_frequent_failures_on_buy_now_page(self):
        self.basePage = BasePage(self.driver)
        self.driver.get(self.buyNowURL)
        self.basePage.wait_for_page_load()
        self.basePage.verify_broken_images()

    # @pytest.mark.smoke
    # @pytest.mark.regression
    def test_006_frequent_failures_on_landing_page(self):
        self.logger.info("Test_006_frequent_failures_on_landing_page")
        self.basePage = BasePage(self.driver)
        self.logger.info("Verify broken images on Software Engineering Online Landing page")
        self.driver.get(self.lpSoftwareEngineerOnlineURL)
        self.basePage.wait_for_page_load()
        time.sleep(3)
        ActionChains(self.driver).move_by_offset(20, 20).click().perform()
        self.basePage.verify_broken_images()
        self.logger.info("Verify broken images on UX UI Online Landing page")
        self.driver.get(self.lpUXUIOnlineURL)
        self.basePage.wait_for_page_load()
        self.basePage.verify_broken_images()

    @pytest.mark.smoke
    # @pytest.mark.regression
    def test_007_frequent_failures_on_elevate_self_paced_page(self):
        self.logger.info("Test_006_frequent_failures_on_landing_page")
        self.basePage = BasePage(self.driver)
        self.logger.info("Verify accordions presence on Elevate Self Paced page")
        self.driver.get(self.cxSelfPacedElevateURL)
        self.basePage.wait_for_page_load()
        time.sleep(3)
        ActionChains(self.driver).move_by_offset(20, 20).click().perform()
        self.elevateSelfPacedPage = ElevateSelfPacedPage(self.driver)
        ActionChains(self.driver).move_by_offset(20, 20).release().perform()
        self.elevateSelfPacedPage.verify_accordions()
