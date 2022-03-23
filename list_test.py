from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')
driver.get("http://suninjuly.github.io/selects1.html")

x_element = driver.find_element(By.ID, 'num1')
y_element = driver.find_element(By.ID, 'num2')
a = x_element.text
b = y_element.text
a = int(a)
b= int(b)
z = a+b
print(z)




select = driver.find_element(By.CLASS_NAME,"custom-select").click()
driver.find_element(By.CSS_SELECTOR , f'[value= "{z}"]').click()
driver.find_element(By.CLASS_NAME , 'btn.btn-default').click()


