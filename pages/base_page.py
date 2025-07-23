from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver: WebDriver, url: str = None):
        """
        Initializes the BasePage with a WebDriver instance and an optional URL.
        """
        self.driver = driver
        if url:
            self.driver.get(url)

    def find_element(self, locator: tuple, time: int = 10) -> WebElement:
        """
        Finds a web element with an explicit wait.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator: tuple, time: int = 10) -> list[WebElement]:
        """
        Finds web elements with an explicit wait.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )
    
    def wait_for_visibility(self, locator: tuple, time: int = 10) -> WebElement:
        """
        Waits for a web element to be visible.
        """
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Element with locator {locator} is not visible"
        )

    def wait_for_invisibility(self, locator: tuple, time: int = 10) -> bool:
        """
        Waits for a web element to be invisible.
        """
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator),
            message=f"Element with locator {locator} is still visible"
        )

    def click(self, locator: tuple, time: int = 10):
        """
        Clicks a web element after ensuring it's clickable.
        """
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Element with locator {locator} is not clickable"
        )
        element.click()

    def enter_text(self, locator: tuple, text: str, time: int = 10):
        """
        Sends keys to a web element after waiting for its visibility.
        """
        element = self.wait_for_visibility(locator, time)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple, time: int = 10) -> str:
        """
        Gets the text of a web element.
        """
        element = self.wait_for_visibility(locator, time)
        return element.text

    def get_current_url(self) -> str:
        """
        Returns the current URL.
        """
        return self.driver.current_url

    def scroll_to_element(self, locator: tuple):
        """
        Scrolls the page to the given element.
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def scroll_to_bottom(self):
        """
        Scrolls the page to the bottom.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """
        Scrolls the page to the top.
        """
        self.driver.execute_script("window.scrollTo(0, 0);")

    def hover_over_element(self, locator: tuple, time: int = 10):
        """
        Hovers the mouse over a web element.
        """
        element = self.find_element(locator, time)
        ActionChains(self.driver).move_to_element(element).perform()

    def accept_alert(self):
        """
        Accepts the browser alert.
        """
        self.driver.switch_to.alert.accept()
