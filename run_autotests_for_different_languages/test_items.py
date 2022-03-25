from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_contains_an_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert 'Ajouter au panier' or button.text
