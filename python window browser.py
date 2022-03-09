from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')
browser.get("http://suninjuly.github.io/redirect_accept.html")
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    button1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()

    new_window = browser.window_handles[1]

    window1 = browser.switch_to.window(new_window) #Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти\


    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button2 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()



finally:
    time.sleep(10)
    browser.quit()



#new_window = browser.window_handles[1] # чтобы узнать имя новой вкладки, нужно использовать метод window_handles

#first_window = browser.window_handles[0] #Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться

