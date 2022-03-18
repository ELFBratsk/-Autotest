import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nСтарт браузера")
    browser = webdriver.Chrome(r'C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')

    yield browser
    print("\nЗакрытие браузера")
    browser.quit()

@pytest.fixture()
def test_1() :
    print("Моя фикстура")

@pytest.fixture(autouse=True) # выполняется для каждого тетста, без явного вызова
def prepare_data():
    print("Выполнение")
    print("Это автофикстура")
    print("Третья надпись")


class TestMainPage1():
    def test_guest_should_see_login_link(self, test_1,browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")