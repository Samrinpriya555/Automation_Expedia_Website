from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail&hl=en&dsh=S-1274824298%3A1621548270242570&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

inputboxes = driver.find_elements(By.CLASS_NAME,'Xb9hP')
print(len(inputboxes))
f_name= driver.find_element_by_id('firstName').send_keys('Selenium')
l_name= driver.find_element_by_id('lastName').send_keys('Testing')
username= driver.find_element_by_id('username').send_keys('Seleniumtesting8080')
password = driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys("kghospital8080")
confirmed_password = driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys("kghospital8080")
show_password = driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div[1]/div/div/div[1]/div').click()




#f_name= driver.find_element_by_id('firstName').is_enabled()
#print(f_name)
#driver.close()


