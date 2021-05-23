from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("https://www.expedia.com/")
links= driver.find_elements(By.TAG_NAME,'a')
print(len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT,"Cars").click()
