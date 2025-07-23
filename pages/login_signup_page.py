from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginSignupPage(BasePage):
    """
    Page Object for the Login/Signup Page.
    """
    # Locators
    NEW_USER_SIGNUP_HEADER = (By.XPATH, "//h2[text()='New User Signup!']")
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Login to your account']")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")
    SIGNUP_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Email Address already exist!')]")


    def get_new_user_signup_header(self):
        return self.get_text(self.NEW_USER_SIGNUP_HEADER)

    def signup(self, name, email):
        self.enter_text(self.SIGNUP_NAME_INPUT, name)
        self.enter_text(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def get_login_header(self):
        return self.get_text(self.LOGIN_HEADER)

    def login(self, email, password):
        self.enter_text(self.LOGIN_EMAIL_INPUT, email)
        self.enter_text(self.LOGIN_PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_login_error_message(self):
        return self.get_text(self.LOGIN_ERROR_MESSAGE)

    def get_signup_error_message(self):
        return self.get_text(self.SIGNUP_ERROR_MESSAGE)
