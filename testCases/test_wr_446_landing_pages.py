import time

import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class TestSubmitLandingPages:
    baseURL = ReadConfig.getApplicationURL("instapageLandingPagesURL")
    logger = LogGen.loggen()

    partnersOnlineCoursesURL = ReadConfig.getApplicationPartnerURL("Online Courses Landing Page")
    partnersCustomerURL = ReadConfig.getApplicationPartnerURL("Customer Experience Landing Page")
    partnersDesignThinkingURL = ReadConfig.getApplicationPartnerURL("Design Thinking Landing Page")
    partnersCyberURL = ReadConfig.getApplicationPartnerURL("Cyber Security Engineering Landing Page")
    partnersGraphicURL = ReadConfig.getApplicationPartnerURL("Graphic Design Landing Page")
    partnersDigitalMarketingURL = ReadConfig.getApplicationPartnerURL("Digital Marketing Landing Page")
    partnersSociaMediaMarketinglURL = ReadConfig.getApplicationPartnerURL("Social Media Marketing Landing Page")
    partnersProjectURL = ReadConfig.getApplicationPartnerURL("Project Management Landing Page")
    partnersServiceDesignURL = ReadConfig.getApplicationPartnerURL("Service Design Landing Page")
    partnersDataAnalyticsURL = ReadConfig.getApplicationPartnerURL("Data Analytics Landing Page")
    partnersFrontEndURL = ReadConfig.getApplicationPartnerURL("Front-end Web Development Landing Page")
    partnersSoftwareEngineeringURL = ReadConfig.getApplicationPartnerURL("Software Engineering Landing Page")
    partnersUxUiURL = ReadConfig.getApplicationPartnerURL("UxUi Design Landing Page")

    @pytest.mark.landing_pages
    def test_001_submit_online_courses_landing_page(self):
        self.logger.info("test_001_submit_online_courses_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersOnlineCoursesURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', 'Customer Experience')

    @pytest.mark.landing_pages
    def test_002_submit_customer_experience_landing_page(self):
        self.logger.info("test_002_submit_customer_experience_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersCustomerURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', '')

    @pytest.mark.landing_pages
    def test_003_submit_design_thinking_landing_page(self):
        self.logger.info("test_003_submit_design_thinking_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersDesignThinkingURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', '')

    @pytest.mark.landing_pages
    def test_004_submit_cyber_security_landing_page(self):
        self.logger.info("test_004_submit_cyber_security_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersCyberURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', '', '')

    @pytest.mark.landing_pages
    def test_005_submit_graphic_design_landing_page(self):
        self.logger.info("test_005_submit_graphic_design_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersGraphicURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', '')

    @pytest.mark.landing_pages
    def test_006_submit_digital_marketing_landing_page(self):
        self.logger.info("test_006_submit_digital_marketing_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersDigitalMarketingURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', 'Digital Marketing')

    @pytest.mark.landing_pages
    def test_007_submit_socia_media_marketing_landing_page(self):
        self.logger.info("test_007_submit_socia_media_marketing_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersSociaMediaMarketinglURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', 'Social Media Marketing')

    # @pytest.mark.landing_pages
    def test_008_submit_project_management_landing_page(self):
        self.logger.info("test_008_submit_project_management_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersProjectURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', 'Social Media Marketing')

    @pytest.mark.landing_pages
    def test_009_submit_service_design_landing_page(self):
        self.logger.info("test_009_submit_service_design_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersServiceDesignURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', '')

    @pytest.mark.landing_pages
    def test_010_submit_data_analytics_landing_page(self):
        self.logger.info("test_010_submit_data_analytics_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersDataAnalyticsURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', '')

    @pytest.mark.landing_pages
    def test_011_submit_front_end_web_development_landing_page(self):
        self.logger.info("test_011_submit_front_end_web_development_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersFrontEndURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', '')

    @pytest.mark.landing_pages
    def test_012_submit_software_engineering_landing_page(self):
        self.logger.info("test_012_submit_software_engineering_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersSoftwareEngineeringURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', 'Software Engineering')

    @pytest.mark.landing_pages
    def test_013_submit_ux_ui_design_landing_page(self):
        self.logger.info("test_013_submit_ux_ui_design_landing_page")
        self.homePage = HomePage(self.driver)
        self.homePage.download_course_guide_landing_page(self.partnersUxUiURL, 'sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career', 'Within 6 months', '')

