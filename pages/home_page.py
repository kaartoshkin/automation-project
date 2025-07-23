from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    Page Object for the Home Page.
    """
    URL = "http://automationexercise.com/"
    
    # Locators
    LOGO = (By.CSS_SELECTOR, "img[alt='Website for practice automation']")
    SIGNUP_LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    LOGGED_IN_AS = (By.XPATH, "//li/a[contains(text(), 'Logged in as')]")
    DELETE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/delete_account']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, "a[href='/contact_us']")
    TEST_CASES_BUTTON = (By.CSS_SELECTOR, "a[href='/test_cases']")
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a[href='/products']")
    CART_BUTTON = (By.CSS_SELECTOR, "a[href='/view_cart']")
    FIRST_PRODUCT_VIEW_LINK = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    SUBSCRIPTION_TEXT = (By.XPATH, "//h2[text()='Subscription']")
    SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MSG = (By.ID, "success-subscribe")
    RECOMMENDED_ITEMS_HEADER = (By.XPATH, "//h2[text()='recommended items']")
    ADD_TO_CART_RECOMMENDED = (By.CSS_SELECTOR, "div.recommended_items .item.active a.add-to-cart")
    VIEW_CART_MODAL_LINK = (By.CSS_SELECTOR, "p > a[href='/view_cart']")
    SCROLL_UP_ARROW = (By.ID, "scrollUp")
    CAROUSEL_TEXT = (By.XPATH, "//div[@class='item active']//h2[contains(text(),'Full-Fledged practice website')]")

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def is_home_page_visible(self):
        return self.find_element(self.LOGO).is_displayed()

    def go_to_login_signup_page(self):
        self.click(self.SIGNUP_LOGIN_BUTTON)
    
    def get_logged_in_user(self):
        return self.get_text(self.LOGGED_IN_AS)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BUTTON)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def go_to_contact_us(self):
        self.click(self.CONTACT_US_BUTTON)

    def go_to_test_cases(self):
        self.click(self.TEST_CASES_BUTTON)

    def go_to_products(self):
        self.click(self.PRODUCTS_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)

    def view_first_product(self):
        self.click(self.FIRST_PRODUCT_VIEW_LINK)

    def scroll_to_subscription(self):
        self.scroll_to_element(self.SUBSCRIPTION_TEXT)
    
    def get_subscription_text(self):
        return self.get_text(self.SUBSCRIPTION_TEXT)
        
    def subscribe_with_email(self, email):
        self.enter_text(self.SUBSCRIPTION_EMAIL_INPUT, email)
        self.click(self.SUBSCRIPTION_BUTTON)
    
    def get_subscription_success_message(self):
        return self.get_text(self.SUBSCRIPTION_SUCCESS_MSG)

    def is_recommended_items_visible(self):
        return self.find_element(self.RECOMMENDED_ITEMS_HEADER).is_displayed()

    def add_recommended_product_to_cart(self):
        self.click(self.ADD_TO_CART_RECOMMENDED)

    def view_cart_in_modal(self):
        self.click(self.VIEW_CART_MODAL_LINK, time=5)

    def click_scroll_up_arrow(self):
        self.click(self.SCROLL_UP_ARROW)
    
    def is_carousel_text_visible(self):
        return self.wait_for_visibility(self.CAROUSEL_TEXT).is_displayed()
