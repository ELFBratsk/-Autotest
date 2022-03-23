import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import pyautogui



driver: WebDriver = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver.exe")






driver.get('http://ft1-rd.g4lab.com/rd/login')

search_field = driver.find_element_by_name("_username")
search_field.send_keys(email_test)

search_field = driver.find_element_by_name("_password")
search_field.send_keys(password)

search_field.send_keys(Keys.RETURN)





search_field = driver.find_element_by_name("_username")
search_field.send_keys(email_test)

search_field = driver.find_element_by_name("_password")
search_field.send_keys(password)

search_field.send_keys(Keys.RETURN)

add_to_cart_button = driver.find_element_by_xpath('//*[@id="complete_combobox_contract_region"]')
add_to_cart_button.click()

add_to_cart_button = driver.find_element_by_xpath('//*[@id="dk_container_contract_region"]/div/ul/li[2]/a')
add_to_cart_button.click()

add_to_cart_button = driver.find_element_by_xpath('//*[@id="form_id"]/div[2]/div[2]/div/div/div/span')
add_to_cart_button.click()

ICCID = driver.find_element_by_xpath('//*[@id="contract_mnp_device_id"]')
ICCID.click()
ICCID.send_keys('0200441535')


old_number = driver.find_element_by_name('contract[mnp][msisdn]')

old_number.click()
old_number.send_keys('9999999999')



name_operator = driver.find_element_by_name('contract[mnp][operator]')


name_operator.click()


name_operator.send_keys('а')


name_operator.send_keys(Keys.RETURN)

name = driver.find_element_by_name('contract[client_data][name_data_raw]')
name.send_keys('Евгений Орлов Валерьевич')

date_brith = driver.find_element_by_name('contract[client_data][birth_date]')
date_brith.send_keys('12.12.2001')



birth_place = driver.find_element_by_name('contract[client_data][birth_place]')
birth_place.send_keys('Ангарск')

document_number_raw = driver.find_element_by_name('contract[client_data][document_department_code]')
document_number_raw.replace()
document_number_raw.send_keys('4515256399')

document_department_code = driver.find_element_by_name('contract[client_data][document_department_code]')
document_department_code.clear()
document_department_code.send_keys('111')






document_issue_date = driver.find_element_by_name('contract[client_data][document_issue_date]')
old_number.click()
document_issue_date.send_keys('12.01.2016')

document_issued_by = driver.find_element_by_name('contract[client_data][document_issued_by]')
document_issued_by.send_keys('УФМС Орска')

residence_address = driver.find_element_by_name('contract[client_data][residence_address]')
residence_address.send_keys('СПб, Дальневосточный проспект, 25к1м. Улица Дыбенко')

email = driver.find_element_by_name('contract[client_data][email]')
email.send_keys('email@email.ru')

contact_phone = driver.find_element_by_name('contract[client_data][contact_phone]')
contact_phone.send_keys('999 999 9999')















