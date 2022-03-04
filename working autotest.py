from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

url = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("")

driver.get(url)
email_test = ''
password = ''

search_field = driver.find_element_by_name("_username")
search_field.send_keys(email_test)

search_field = driver.find_element_by_name("_password")
search_field.send_keys(password)
search_field.send_keys(Keys.RETURN)

driver.execute_script("$('*').unmask(); $('*').inputmask('remove')")

add_to_cart_button = driver.find_element_by_xpath('//*[@id="complete_combobox_contract_region"]')
add_to_cart_button.click()

add_to_cart_button = driver.find_element_by_xpath('//*[@id="dk_container_contract_region"]/div/ul/li[2]/a')
add_to_cart_button.click()

add_to_cart_button = driver.find_element_by_xpath('//*[@id="form_id"]/div[2]/div[2]/div/div/div/span')
add_to_cart_button.click()

ICCID = driver.find_element_by_xpath('//*[@id="contract_mnp_device_id"]')
ICCID.click()
ICCID.send_keys('0200441558')

old_number = driver.find_element_by_name('contract[mnp][msisdn]')

old_number.click()
old_number.send_keys('')

name_operator = driver.find_element_by_name('contract[mnp][operator]')

name_operator.click()

name_operator.send_keys('а')
name_operator.send_keys(Keys.RETURN)

date_brith = driver.find_element_by_name('contract[client_data][birth_date]')
date_brith.send_keys('')

birth_place = driver.find_element_by_name('contract[client_data][birth_place]')
birth_place.send_keys('Ангарск')

document_number_raw = driver.find_element_by_name('contract[client_data][document_number_raw]')

document_number_raw.send_keys('')

document_department_code = driver.find_element_by_name('contract[client_data][document_department_code]')
document_department_code.clear()
document_department_code.send_keys('')

document_issue_date = driver.find_element_by_name('contract[client_data][document_issue_date]')
old_number.click()
document_issue_date.send_keys('')

document_issued_by = driver.find_element_by_name('contract[client_data][document_issued_by]')
document_issued_by.send_keys('')

residence_address = driver.find_element_by_name('contract[client_data][address]')
residence_address.send_keys('')

email = driver.find_element_by_name('contract[client_data][email]')
email.send_keys('')

contact_phone = driver.find_element_by_name('contract[client_data][contact_phone]')
contact_phone.send_keys('')

name = driver.find_element_by_name('contract[client_data][name_data_raw]')
name.send_keys('')

print_id = driver.find_element_by_xpath('//*[@id="print_id"]')
print_id.click()


time.sleep(5)

driver.switch_to.window(driver.window_handles[2])


#dowlound_pdf=driver.find_element_by_css_selector('"method":"css selector" [name="icon > iron-icon"]')
#dowlound_pdf.click()
##icon > iron-icon

driver.find_element_by_xpath('//*[@id="icon"]').click()
