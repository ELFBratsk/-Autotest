from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\\data_test\\chromedriver.exe')
link = " http://SunInJuly.github.io/execute_script.html"
driver.get(link)
button = driver.find_element_by_tag_name("button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()