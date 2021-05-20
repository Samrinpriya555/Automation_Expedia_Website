from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path='/usr/bin/chromedriver')

driver.get('https://duckduckgo.com/?va=b&t=hc')

print(driver.title)

driver.get('https://mail.google.com/mail/u/1/#inbox')
print(driver.title)

driver.back()
print(driver.title)
driver.forward()
print(driver.title)
