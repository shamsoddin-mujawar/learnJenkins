import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    """Setup and teardown for Selenium WebDriver"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def test_google_title(driver):
    """Verify Google homepage title"""
    assert "Google" in driver.title

def test_feeling_lucky_button(driver):
    """Verify 'I'm Feeling Lucky' button is present"""
    lucky_button = driver.find_element(By.XPATH, "(//input[@name='btnI'])[2]")
    assert lucky_button.is_displayed()

def test_google_search(driver):
    """Search for a keyword and verify results"""
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    assert "Selenium" in driver.page_source

