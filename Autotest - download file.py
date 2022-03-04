from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome('')

    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('IVAN')

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('IVAN')

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('1@mail.ru')



    current_dir = os.path.abspath(os.path.dirname(''))  # получаем путь к директории текущего исполняемого файла
    file_name = "file.txt" # имя файла в переменной

    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys('')  # # добавляем к этому пути имя файла


    button = browser.find_element(By.TAG_NAME, 'button').click()

finally :
    time.sleep(10)
    browser.quit()
