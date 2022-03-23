import time
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome(r'C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.XPATH, "//input[@class='form-control first']")
        input1.send_keys('новости')

        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second']")
        input2.send_keys('новости')

        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
        input3.send_keys('новости')

        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys('новости')

        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys('новости')

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

    def test_abs2(self):
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.XPATH, "//input[@class='form-control first']")
        input1.send_keys('новости')

        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second']")
        input2.send_keys('новости')

        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
        input3.send_keys('новости')

        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys('новости')

        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys('новости')

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


if __name__ == "__main__":
    unittest.main()
    # browser.quit()
