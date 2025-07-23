from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountCreatedPage(BasePage):
    """
    Page Object for the Account Created confirmation Page.
    """
    # Locators
    ACCOUNT_CREATED_HEADER = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    ACCOUNT_DELETED_HEADER = (By.XPATH, "//b[text()='Account Deleted!']")

    def get_account_created_header(self):
        return self.get_text(self.ACCOUNT_CREATED_HEADER)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def get_account_deleted_header(self):
        return self.get_text(self.ACCOUNT_DELETED_HEADER)
