import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://www.expedia.com/')
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="uitk-tabs-button-container"]/li[2]/a/span').click()




driver.find_element(By.CLASS_NAME,'uitk-faux-input').send_keys('Berlin (BER - Brandenburg)')
print("entered data")

wait = WebDriverWait(driver,10)
allitem = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="location-field-leg1-origin-menu"]/div[2]/ul')))
for item in allitem:
    item.click()
    break

destination = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="location-field-leg1-destination-menu"]/div[1]/button'))).send_keys('Dhaka (DAC - Shahjalal Intl.)')

des_item= wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]/button')))
for item in des_item:
    item.click()
    break



#driver.des.send_keys('Dhaka (DAC - Shahjalal Intl.)')


#des = wait.until(EC.element_to_be_selected((By.XPATH,'//*[@id="location-field-leg1-destination"]')))
#des.send_keys('Dhaka (DAC - Shahjalal Intl.)')


# time.sleep(7)
# items = driver.find_element_by_tag_name("ul")
# for item in items:
#     print(item.text)
# item  = Select(driver.find_element(By.CLASS_NAME,'uitk-typeahead-results'))
# item.selectByIndex(0).click()
#driver.find_element(By.XPATH,'//*[@id="location-field-leg1-origin-menu"]/div[2]/ul')
#elem= driver.find_element(By.TAG_NAME,'//*[@id="location-field-leg1-origin-menu"]/div[2]/ul')
#all_opts= elem.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[0]').click()

#driver.find_element(By.CLASS_NAME,'uitk-button uitk-button-medium uitk-button-fullWidth uitk-button-typeahead uitk-type-left has-subtext').click()
#time.sleep(3)


#driver.find_element(By.XPATH,'//*[@id="location-field-leg1-destination"]').send_keys('Dhaka (DAC - Shahjalal Intl.)')
#time.sleep(10)


date_select = wait.until(EC.element_to_be_clickable((By.ID,'d1-btn'))).click()
time.sleep(2)
start_date= driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[4]/button').click()
time.sleep(2)
end_date= driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/button').click()
done = driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[3]/button/span').click()
print("where is input")
driver.find_element(By.XPATH,'//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()

#wait= WebDriverWait(driver,10)


#emirat = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-layer-base"]/div[2]/div[3]/div[1]/aside/fieldset/fieldset[3]/div[2]/div/div[1]/div/div[2]')))




