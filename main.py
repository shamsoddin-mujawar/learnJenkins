from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
# REMOVE or COMMENT OUT this line:
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")

driver.quit()
