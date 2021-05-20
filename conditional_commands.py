from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path='/usr/bin/chromedriver')

driver.get('https://www.overleaf.com/login')

username = driver.find_element_by_name('email')

print(username.is_enabled())
print(username.is_displayed())

username.send_keys('samrinpriya555@gmail.com')
password = driver.find_element_by_name('password')

print(password.is_enabled())
print(password.is_displayed())

password.send_keys('13301101samrin')


driver.find_element_by_xpath('/html/body/div/main/div/form/div[3]/button').click()

project_type = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[1]/aside/div[2] ')

for pro_item in project_type:
    print(pro_item.title)







