from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

import unittest

browser = webdriver.Chrome(r'C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')
browser.get('http://suninjuly.github.io/registration2.html')


class Test(unittest.TestCase):

    def test_unit(self):
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys('новости')

        input2 = browser.find_element(By.CLASS_NAME, "form-control.third")
        input2.send_keys('новости')

        input3 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.second_block > div.form-group.first_class > input")
        input3.send_keys('новости')

        input4 = browser.find_element(By.CLASS_NAME, "form-control.second")
        input4.send_keys('новости')

        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys('новости')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        h1 = browser.find_element_by_tag_name('h1')
        h2 = h1.text
        print(h2)
        h3 = 'Congratulations! You have successfully registered!'

        self.assertEqual(h2 == h3, True)


        browser.quit()

if __name__ == "__main__":
    unittest.main()
