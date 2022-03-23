from selenium import webdriver
import time
from selenium.webdriver.common.by import By





browser = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver.exe")

browser.get('http://suninjuly.github.io/find_xpath_form')

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")

input2 = browser.find_element_by_name('last_name')
input2.send_keys("Petrov")

input3 =browser.find_element(by=By.CLASS_NAME, value='city:form-control')

input3.send_keys("Smolensk")
input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")
button = browser.find_element_by_css_selector('//button[text()="Submit"]')
button.click()


    # успеваем скопировать код за 30 секунд
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла