import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    """
    Page Object for the Contact Us Page.
    """
    # Locators
    GET_IN_TOUCH_HEADER = (By.XPATH, "//h2[text()='Get In Touch']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    UPLOAD_FILE_BUTTON = (By.NAME, "upload_file")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.status.alert.alert-success")
    HOME_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-success")

    def get_get_in_touch_header(self):
        return self.get_text(self.GET_IN_TOUCH_HEADER)

    def fill_contact_form(self, name, email, subject, message):
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.SUBJECT_INPUT, subject)
        self.enter_text(self.MESSAGE_TEXTAREA, message)

    def upload_file(self, file_path):
        self.find_element(self.UPLOAD_FILE_BUTTON).send_keys(file_path)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def go_to_home(self):
        self.click(self.HOME_BUTTON)
