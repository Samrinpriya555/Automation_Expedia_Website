import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get('https://duckduckgo.com/?va=b&t=hc')
print(driver.title)
driver.find_element_by_xpath('//*[@id="content_homepage"]/div[2]/div/div/a[1]/span').click()
time.sleep(10)
driver.close()
#driver.quit()/ closes all browser