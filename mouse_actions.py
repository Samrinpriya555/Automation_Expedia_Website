from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
wait = WebDriverWait(driver,10)
wait = WebDriverWait(driver,10)

actions = ActionChains(driver)
driver.get("https://www.expedia.com/")
driver.maximize_window()
More_Travel = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gc-custom-header-tool-bar-shop-menu"]/button/div'))).click()
stays = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gc-custom-header-tool-bar-shop-menu"]/div/div/a[1]')))
Flight = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gc-custom-header-tool-bar-shop-menu"]/div/div/a[2]')))
actions.move_to_element(stays).move_to_element(Flight).click().perform()
