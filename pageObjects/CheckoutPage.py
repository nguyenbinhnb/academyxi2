import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class CheckoutPage(BasePage):
    logger = LogGen.loggen()
    textbox_firstname_id = "billing_first_name"
    textbox_lastname_id = "billing_last_name"
    street_address_css_selector = "input[name*='billing_address']"
    phone_id = "billing_phone"
    email_address_id = "billing_email"
    dob_date_css_selector = "span[aria-labelledby*='select2-billing_day-container']"
    dob_month_id = "billing_month_field"
    dob_year_css_selector = "span[aria-labelledby*='select2-billing_year-container']"
    input_textbox_class_name = "select2-search__field"
    h2_with_text = "//h2[text()='{}']"
    li_text_xpath = "//li[text()='{}']"
    next_button = "//button[@class= 'checkout-action-next']"
    chat_box_iframe = "//iframe[@id='chat-widget']"
    minimize_icon = "//button[@aria-label='Minimize window']"
    term_check_box = "//input[@id= 'chk_term']"
    a_with_class = "//a[@class='{}']"
    span_with_text = "//span[text()='{}']"
    payment_options = "//div[contains(@class, 'item-product') ]"
    add_to_cart_button = "(//div[contains(@class, 'btn-addtocart')])[{}]"
    h3_with_text = "//h3[text()='{}']"
    p_with_text = "//p[text()='{}']"
    td_with_text = "//td[text()='{}']"
    price = "(//td//span[contains(@class,'woocommerce-Price-amount')])[{}]"
    card_name = "//input[@id='stripe-card-name']"
    card_number = "//input[@id='stripe-card-number']"
    expiry = "//input[@id='stripe-card-expiry']"
    card_code = "//input[@id='stripe-card-cvc']"
    title = "//p[@id='billing_title_field']"
    label_with_text = "//label[text()='{}']"
    input_with_id = "//input[@id='{}']"
    th_with_text = "//th[text()='{}']"
    p_contains_text = "//p[contains(text(),'{}')]"
    button_contains_class = "//button[contains(@class,'{}')]"

    def __init__(self, driver):
        self.driver = driver
        self.element_by_finder = ElementByLocator()

    def set_first_name(self, firstname):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.ID, self.textbox_firstname_id))).clear()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, self.textbox_firstname_id))).send_keys(firstname)

    def set_last_name(self, lastname):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.textbox_lastname_id))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.textbox_lastname_id))).send_keys(lastname)

    def set_street_address(self, address):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.street_address_css_selector))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.street_address_css_selector))).send_keys(address)

    def set_phone(self, phone):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.phone_id))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.phone_id))).send_keys(phone)

    def set_bod(self, bod):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "billing_date_of_birth"))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "billing_date_of_birth"))).send_keys(bod)

    def set_email_address(self, email):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.email_address_id))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.email_address_id))).send_keys(email)

    def set_date(self, date):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.dob_date_css_selector))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(date)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(date)))).click()

    def set_month(self, month):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.ID, self.dob_month_id))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(month)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(month)))).click()

    def set_year(self, year):
        element = self.driver.find_element(By.ID, 'billing_phone')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.dob_year_css_selector))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(year)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(year)))).click()

    def fill_in_details_for_checkout(self):
        self.scroll_into_view(self.title)
        self.set_first_name('Sandbox')
        self.set_last_name("Axi Testing")
        self.set_street_address("123 hanoi")
        self.set_phone("392328789")
        self.set_email_address("binh.n@academyxi.com")
        self.close_chat_box()
        self.input_text(self.input_with_id.format("billing_date_of_birth"), "11/11/1999")
        self.scroll_into_view(self.next_button)
        self.click_element_by_js(self.next_button)

    def close_chat_box(self):
        if self.is_visible(self.chat_box_iframe, timeout=2):
            self.switch_to_iframe(self.chat_box_iframe)
            self.click_element_by_js(self.minimize_icon)
            self.driver.switch_to.default_content()

    def verify_payment_options(self):
        payment_list = self.driver.find_elements(By.XPATH, self.payment_options)
        assert len(payment_list) >= 2
        self.logger.info("There are {} payment options on Checkout Page".format(len(payment_list)))

    def choose_payment_option(self, num):
        self.click_element_by_js(self.add_to_cart_button.format(num))
        if self.is_present(self.a_with_class.format('btn-review')):
            self.click_element_by_js(self.a_with_class.format('btn-review'))
        self.wait_for_loading_icon_disappear()

    def verify_payment_summary(self):
        self.scroll_into_view(self.label_with_text.format("Payment summary:"))
        self.element_should_be_present(self.label_with_text.format("Payment summary:"))
        self.element_should_be_present(self.p_contains_text.format('Course fee'))
        self.element_should_be_present(self.td_with_text.format('Total AUD (inc. tax)'))
        self.element_should_be_present(self.price.format('1'))
        self.element_should_be_present(self.price.format('2'))
        self.element_should_be_present(self.price.format('3'))


    def fill_in_details_for_payment_and_submit(self):
        self.input_text(self.card_name, "Test")
        self.input_text(self.card_number, "4242")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.card_number))).send_keys("4242")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.card_number))).send_keys("4242")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.card_number))).send_keys("4242")
        self.input_text(self.expiry, "09")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.expiry))).send_keys("25")
        self.input_text(self.card_code, "123")
        self.click_element(self.input_with_id.format("chk_term"))
        self.scroll_into_view(self.button_contains_class.format("btn-confirm"))
        self.click_element(self.button_contains_class.format("btn-confirm"))
        self.wait_for_loading_icon_disappear()

    def verify_that_enrolment_is_confirmed(self):
        self.wait_element_presence("//p[contains(text(),'Application number')]")
        self.element_should_be_present(self.h2_with_text.format("Your enrolment is confirmed"))


