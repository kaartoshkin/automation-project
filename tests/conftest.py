import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to initialize and quit the WebDriver for each test function.
    """
    # Setup: Initialize the WebDriver using webdriver-manager
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Uncomment for headless execution
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    
    # Teardown: Quit the WebDriver after the test is done
    driver.quit()
