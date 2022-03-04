from selenium import webdriver
import time

browser = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')
browser.get("http://suninjuly.github.io/huge_form.html")



try:

    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:

    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
