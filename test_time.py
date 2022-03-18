import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


@pytest.mark.parametrize('list', ["236895", "236896"]) #236897 , 236898 , 236899 , 236903,236904 ,236905"])
class Test():

    def test_guest_should_see_login_link(self, browser, list):
        answer = str(math.log(int(time.time())))



        link = f"https://stepik.org/lesson/{list}/step/1"
        browser.get(link)
        browser.implicitly_wait(15)
        browser.find_element(By.CSS_SELECTOR, "[id='ember86']").send_keys(answer)

        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        #alert = browser.switch_to.alert
        #alert_text = alert.text
        #assert alert_text == 'Correct'
        time.sleep(5)
