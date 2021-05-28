from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
wait = WebDriverWait(driver,10)
driver.get("https://www.expedia.com/Hotel-Search?destination=Frankfurt%20%28and%20vicinity%29%2C%20Hessen%2C%20Germany&endDate=2021-11-19&paandi=true&paymentType=FREE_CANCELLATION&regionId=179894&rfrr=page.Hotels.0.Hotel.1.17008.d34d0a03-bd37-433e-99ec-fc1894866834.f2e29c0d-a1ef-4fd8-8f1f-f0068ea6f555.2&selected=50719241&semdtl=&sort=RECOMMENDED&startDate=2021-11-17&theme=&useRewards=false&userIntent=")
driver.maximize_window()
w = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-layer-base"]/div/main/div/div/div[1]/section/div[2]/div/div[2]/section[2]/ol/li[1]/div/section[2]/span/div/div/div[2]/figure/button'))).click()

print(driver.current_window_handle)

windows = driver.window_handles

for win in windows:
    driver.switch_to.window(win)
    print(driver.title)