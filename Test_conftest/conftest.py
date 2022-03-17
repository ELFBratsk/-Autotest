import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(r'C:\\Users\\user\\PycharmProjects\\data_test\\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()



