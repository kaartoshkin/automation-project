from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestCasesPage(BasePage):
    """
    Page Object for the Test Cases Page.
    """
    # Locators
    TEST_CASES_HEADER = (By.XPATH, "//h2/b[text()='Test Cases']")

    def is_test_cases_page_visible(self):
        return self.find_element(self.TEST_CASES_HEADER).is_displayed()
