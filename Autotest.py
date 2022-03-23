from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import  unittest
try:
    browser = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')
    browser.get('http://suninjuly.github.io/registration2.html')

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
    input1.send_keys('новости')
    input2 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input2.send_keys('новости')

    input3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input")
    input3.send_keys('новости')

    input4 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input4.send_keys('новости')

    input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
    input5.send_keys('новости')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

##browser.quit()
