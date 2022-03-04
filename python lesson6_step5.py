from selenium import webdriver
import math

browser = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')
browser.get("http://suninjuly.github.io/find_link_text")



try:
    number = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    click = browser.find_element_by_link_text(number).click()

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('firstname')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:

    # закрываем браузер после всех манипуляций
    browser.quit()

