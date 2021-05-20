from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
#driver= webdriver.Firefox(executable_path='/usr/bin/geckodriver')
driver.get("https://www.facebook.com/")
print(driver.title)
driver.close()

