import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.maximize_window()

driver.switch_to.frame('packageListFrame')
element_one = driver.find_element(By.LINK_TEXT,'org.openqa.selenium.cli').click()


 
driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT,'WrappedPrintWriter').click()

