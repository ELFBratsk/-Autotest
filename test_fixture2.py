import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture # Фикстура для открывания браузера
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(r'C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')
    return browser


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser): # вызываем фикстуру в тесте, передав ее как параметр
        print('Тест - 1')
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self,browser):
        print('Тест - 2')
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")



#