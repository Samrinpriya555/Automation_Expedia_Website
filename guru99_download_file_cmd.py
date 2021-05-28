from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("https://www.guru99.com/test-case.html")
driver.maximize_window()
wait = WebDriverWait(driver,10)
actions = ActionChains(driver)

Test_Case_Template = driver.find_element(By.XPATH,'//*[@id="g-mainbar"]/div[1]/div/div/div/div/div/div[2]/p[41]/a')
scroll_by_element = driver.execute_script("arguments[0].scrollIntoView();", Test_Case_Template)
Download = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="g-mainbar"]/div[1]/div/div/div/div/div/div[2]/p[41]/a'))).click()