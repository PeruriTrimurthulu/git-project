from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import requests
# broken links
def test_chromedemo():
    driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.orangehrm.com/")
    print("\nTitle",driver.title)
    assert driver.title == "OrangeHRM HR Software | OrangeHRM"
    time.sleep(3)

    list_links = driver.find_elements(By.TAG_NAME,"a")
    for link in list_links:
        url = link.get_attribute("href")
        title = link.text
        try:
            response = requests.get(url,params=None)
            if response.status_code in [200,201]:
                status = "passes"
            else:
                status = "failed"
        except:
            status = "failed"
        row = [title, url, status]
        print(title,"=>",url,"",status)

        with open("links.csv","a") as linksfile:
            csvwriter = csv.writer(linksfile)
            csvwriter.writerow(row)
    time.sleep(2)
    driver.close()



