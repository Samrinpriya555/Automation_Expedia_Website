import xlUtil
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.get("https://www.overleaf.com/login")
driver.maximize_window()

path = "/home/mrony/overleaf_login_cred_valid_invalid.xlsx"

row= xlUtil.getRowcount(path,"Sheet1")
print(row)

for r in range(2, row+1):
    username= xlUtil.readdata(path,"Sheet1",r,1)
    password= xlUtil.readdata(path,"Sheet1",r,2)
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[2]/main/div/form/div[3]/button').click()
    if driver.title=="https://www.overleaf.com/project":
        xlUtil.writedata(path,"Sheet1",r,3,"pass")
    else:
        xlUtil.writedata(path,"Sheet1",r,3,"fail")


    driver.get("https://www.overleaf.com/login")