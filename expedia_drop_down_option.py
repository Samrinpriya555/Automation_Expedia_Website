import select
import time
from typing import Optional, List, Any

from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

driver.get('https://www.expedia.com/')
time.sleep(3)
driver.maximize_window()


time.sleep(5)

more_drop = driver.find_element(By.XPATH,'//*[@id="gc-custom-header-tool-bar-shop-menu"]/button/div').click()

time.sleep(3)
wait = WebDriverWait(driver,20)



all_opt = driver.find_elements(By.CSS_SELECTOR,'#gc-custom-header-tool-bar-shop-menu > div > div > a')
for item in all_opt:
    print(item.get_attribute("href"))


#driver.find_element_by_tag_name('')

#element = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="gc-custom-header-tool-bar-shop-menu"]/div')))

#for item in all_opt:
    #item.get_attribute("href")
#driver.close()
#driver.implicitly_wait(1)
#wait = WebDriverWait(driver,5)
#wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gc-custom-header-tool-bar-shop-menu"]/div/div/a[3]'))).click()

