from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = ChromeOptions()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--app=http://localhost:5000/login")
driver = webdriver.Chrome(options=chrome_options)

WebDriverWait(driver, 300).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'ok')]")))

chromium_cookies = driver.get_cookies()
driver.close()

requests_cookies = {c["name"]: c["value"] for c in chromium_cookies}

import requests

token_response = requests.get("http://localhost:5000/user/token", cookies=requests_cookies)
token_response.raise_for_status()
token = token_response.text
print(token)

userid_response = requests.get("http://localhost:5000/user/id", headers={"Authorization": f"Bearer {token}"})
userid_response.raise_for_status()
print(userid_response.text)

