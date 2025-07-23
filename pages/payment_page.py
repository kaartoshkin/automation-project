from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PaymentPage(BasePage):
    """
    Page Object for the Payment Page.
    """
    # Locators
    NAME_ON_CARD_INPUT = (By.CSS_SELECTOR, "input[data-qa='name-on-card']")
    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-qa='card-number']")
    CVC_INPUT = (By.CSS_SELECTOR, "input[data-qa='cvc']")
    EXPIRATION_MONTH_INPUT = (By.CSS_SELECTOR, "input[data-qa='expiry-month']")
    EXPIRATION_YEAR_INPUT = (By.CSS_SELECTOR, "input[data-qa='expiry-year']")
    PAY_AND_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[data-qa='pay-button']")
    ORDER_PLACED_HEADER = (By.XPATH, "//b[text()='Order Placed']")
    DOWNLOAD_INVOICE_BUTTON = (By.CSS_SELECTOR, "a.check_out")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def fill_payment_details(self, card_details):
        self.enter_text(self.NAME_ON_CARD_INPUT, card_details['name'])
        self.enter_text(self.CARD_NUMBER_INPUT, card_details['number'])
        self.enter_text(self.CVC_INPUT, card_details['cvc'])
        self.enter_text(self.EXPIRATION_MONTH_INPUT, card_details['month'])
        self.enter_text(self.EXPIRATION_YEAR_INPUT, card_details['year'])

    def click_pay_and_confirm(self):
        self.click(self.PAY_AND_CONFIRM_BUTTON)
    
    def get_order_placed_message(self):
        return self.get_text(self.ORDER_PLACED_HEADER)

    def download_invoice(self):
        self.click(self.DOWNLOAD_INVOICE_BUTTON)

    def continue_after_payment(self):
        self.click(self.CONTINUE_BUTTON)
