from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """
    Page Object for the Checkout Page.
    """
    # Locators
    REGISTER_LOGIN_LINK = (By.CSS_SELECTOR, ".modal-body u[href='/login']")
    DELIVERY_ADDRESS_DETAILS = (By.ID, "address_delivery")
    BILLING_ADDRESS_DETAILS = (By.ID, "address_invoice")
    ORDER_REVIEW_TABLE = (By.ID, "cart_info")
    COMMENT_TEXT_AREA = (By.CSS_SELECTOR, "textarea[name='message']")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "a[href='/payment']")

    def click_register_login_on_modal(self):
        self.click(self.REGISTER_LOGIN_LINK)
    
    def get_delivery_address_text(self):
        return self.find_element(self.DELIVERY_ADDRESS_DETAILS).text

    def get_billing_address_text(self):
        return self.find_element(self.BILLING_ADDRESS_DETAILS).text

    def has_order_review(self):
        return self.find_element(self.ORDER_REVIEW_TABLE).is_displayed()

    def enter_comment(self, comment):
        self.enter_text(self.COMMENT_TEXT_AREA, comment)

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)
