from selenium import webdriver
browser = webdriver.Chrome('C:\\Users\\user\\PycharmProjects\\data_test\\chromedriver.exe')

link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 100);")