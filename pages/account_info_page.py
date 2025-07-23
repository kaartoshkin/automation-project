from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class AccountInfoPage(BasePage):
    """
    Page Object for the Account Information Page.
    """
    # Locators
    ACCOUNT_INFO_HEADER = (By.XPATH, "//b[text()='Enter Account Information']")
    TITLE_MR_RADIO = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")
    DAYS_SELECT = (By.ID, "days")
    MONTHS_SELECT = (By.ID, "months")
    YEARS_SELECT = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    PARTNERS_CHECKBOX = (By.ID, "optin")
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS1_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_SELECT = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    
    def get_account_info_header(self):
        return self.get_text(self.ACCOUNT_INFO_HEADER)

    def fill_account_info(self, user_data):
        self.click(self.TITLE_MR_RADIO)
        self.enter_text(self.PASSWORD_INPUT, user_data['password'])
        
        day_select = Select(self.find_element(self.DAYS_SELECT))
        day_select.select_by_visible_text(user_data['dob_day'])
        
        month_select = Select(self.find_element(self.MONTHS_SELECT))
        month_select.select_by_visible_text(user_data['dob_month'])
        
        year_select = Select(self.find_element(self.YEARS_SELECT))
        year_select.select_by_visible_text(user_data['dob_year'])
        
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.PARTNERS_CHECKBOX)
        
        self.enter_text(self.FIRST_NAME_INPUT, user_data['first_name'])
        self.enter_text(self.LAST_NAME_INPUT, user_data['last_name'])
        self.enter_text(self.COMPANY_INPUT, user_data['company'])
        self.enter_text(self.ADDRESS1_INPUT, user_data['address1'])
        self.enter_text(self.ADDRESS2_INPUT, user_data['address2'])
        
        country_select = Select(self.find_element(self.COUNTRY_SELECT))
        country_select.select_by_visible_text(user_data['country'])

        self.enter_text(self.STATE_INPUT, user_data['state'])
        self.enter_text(self.CITY_INPUT, user_data['city'])
        self.enter_text(self.ZIPCODE_INPUT, user_data['zipcode'])
        self.enter_text(self.MOBILE_NUMBER_INPUT, user_data['mobile_number'])
        
        self.click(self.CREATE_ACCOUNT_BUTTON)
