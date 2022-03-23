from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')


# Navigate to url
browser.get("https://www.example.com")

# Retrieves the text of the element
text = browser.find_element(By.CSS_SELECTOR, "h1").text
