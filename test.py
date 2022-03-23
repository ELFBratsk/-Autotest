from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver.exe")
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")



