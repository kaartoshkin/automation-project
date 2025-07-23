from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):
    """
    Page Object for the Shopping Cart Page.
    """
    # Locators
    SUBSCRIPTION_TEXT = (By.XPATH, "//h2[text()='Subscription']")
    SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MSG = (By.ID, "success-subscribe")
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".check_out")
    CART_ITEMS = (By.CSS_SELECTOR, "tbody > tr[id*='product-']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//b[text()='Cart is empty!']")
    SHOPPING_CART_BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb .active")

    def scroll_to_subscription(self):
        self.scroll_to_element(self.SUBSCRIPTION_TEXT)
    
    def get_subscription_text(self):
        return self.get_text(self.SUBSCRIPTION_TEXT)
        
    def subscribe_with_email(self, email):
        self.enter_text(self.SUBSCRIPTION_EMAIL_INPUT, email)
        self.click(self.SUBSCRIPTION_BUTTON)
    
    def get_subscription_success_message(self):
        return self.get_text(self.SUBSCRIPTION_SUCCESS_MSG)
    
    def is_cart_page_visible(self):
        return self.get_text(self.SHOPPING_CART_BREADCRUMB) == "Shopping Cart"

    def get_cart_products(self):
        try:
            return self.find_elements(self.CART_ITEMS, time=3)
        except TimeoutException:
            return []
    
    def get_product_details_by_id(self, product_id):
        row_locator = (By.ID, f"product-{product_id}")
        try:
            row = self.find_element(row_locator, time=3)
            details = {
                "name": row.find_element(By.CSS_SELECTOR, ".cart_description a").text,
                "price": row.find_element(By.CSS_SELECTOR, ".cart_price p").text,
                "quantity": row.find_element(By.CSS_SELECTOR, ".cart_quantity_input").get_attribute('value'),
                "total": row.find_element(By.CSS_SELECTOR, ".cart_total_price").text
            }
            return details
        except TimeoutException:
            return None
        
    def remove_product_by_id(self, product_id):
        remove_button_locator = (By.XPATH, f"//tr[@id='product-{product_id}']//a[@class='cart_quantity_delete']")
        row_locator = (By.ID, f"product-{product_id}")
        self.click(remove_button_locator)
        self.wait_for_invisibility(row_locator)

    def is_cart_empty(self):
        try:
            return self.find_element(self.EMPTY_CART_MESSAGE, time=3).is_displayed()
        except TimeoutException:
            return False

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)
