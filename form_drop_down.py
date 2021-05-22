from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

drp = Select(driver.find_element_by_id('RESULT_RadioButton-9'))
#drp.select_by_index(3)
#drp.select_by_value('Radio-1')
drp.select_by_visible_text('Morning')

all_options = drp.options

for items in all_options:
    print(items.text)