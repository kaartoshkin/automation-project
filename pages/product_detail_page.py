from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    """
    Page Object for the Product Detail Page.
    """
    # Locators
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product-information h2")
    CATEGORY = (By.XPATH, "//p[contains(text(), 'Category:')]")
    PRICE = (By.CSS_SELECTOR, "div.product-information span span")
    AVAILABILITY = (By.XPATH, "//b[text()='Availability:']")
    CONDITION = (By.XPATH, "//b[text()='Condition:']")
    BRAND = (By.XPATH, "//b[text()='Brand:']")
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.cart")
    VIEW_CART_MODAL_LINK = (By.CSS_SELECTOR, "p > a[href='/view_cart']")
    REVIEW_HEADER = (By.XPATH, "//a[text()='Write Your Review']")
    REVIEW_NAME_INPUT = (By.ID, "name")
    REVIEW_EMAIL_INPUT = (By.ID, "email")
    REVIEW_TEXTAREA = (By.ID, "review")
    REVIEW_SUBMIT_BUTTON = (By.ID, "button-review")
    REVIEW_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success span")


    def are_product_details_visible(self):
        self.wait_for_visibility(self.PRODUCT_NAME)
        self.wait_for_visibility(self.CATEGORY)
        self.wait_for_visibility(self.PRICE)
        self.wait_for_visibility(self.AVAILABILITY)
        self.wait_for_visibility(self.CONDITION)
        self.wait_for_visibility(self.BRAND)
        return True
    
    def set_quantity(self, quantity: str):
        self.enter_text(self.QUANTITY_INPUT, quantity)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def view_cart_in_modal(self):
        self.click(self.VIEW_CART_MODAL_LINK)

    def is_write_review_visible(self):
        return self.find_element(self.REVIEW_HEADER).is_displayed()

    def submit_review(self, name, email, review):
        self.enter_text(self.REVIEW_NAME_INPUT, name)
        self.enter_text(self.REVIEW_EMAIL_INPUT, email)
        self.enter_text(self.REVIEW_TEXTAREA, review)
        self.click(self.REVIEW_SUBMIT_BUTTON)
    
    def get_review_success_message(self):
        return self.get_text(self.REVIEW_SUCCESS_MESSAGE)
