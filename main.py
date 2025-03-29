from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# print page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
