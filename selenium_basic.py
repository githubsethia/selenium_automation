#Documentation: https://selenium-python.readthedocs.io/
#Python Selenium Commands Cheat Sheet:
#   http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
#Website Tested below: https://www.seleniumeasy.com/test/ 



from selenium import webdriver
driver = webdriver.Chrome('C:/Users/MXSETH/Desktop/Upgrad_ML_AI/Rough/Selenium/chromedriver.exe')
print(driver)
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in driver.title

button_element = driver.find_element_by_class_name('btn-default')
button_element2 = driver.find_elements_by_css_selector('#get-input > .btn')
print(button_element.get_attribute('innerHTML'))
print(button_element2)

assert 'Show Message' in driver.page_source

message = driver.find_element_by_id('user-message')
message.send_keys("I am awesome!")
button_element.click()

assert 'I am awesome!' in driver.find_element_by_id('display').text

driver.quit()
