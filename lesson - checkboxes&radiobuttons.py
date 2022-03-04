from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome('')
    browser.get('http://suninjuly.github.io/execute_script.html')
    def calc(x):

        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);")


    checkbox =  browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()


    checkbox1 = browser.find_element(By.ID, "robotsRule")
    checkbox1.click()

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





