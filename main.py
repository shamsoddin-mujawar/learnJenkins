from selenium import webdriver

# Set up the WebDriver (Ensure you have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for a few seconds (optional)
import time
time.sleep(5)

# Close the browser
driver.quit()
