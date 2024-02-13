from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#reference  : https://pypi.org/project/webdriver-manager/

def test_chromedemo():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com")
    print("\nTitle ",driver.title)
    time.sleep(3)
    driver.close()