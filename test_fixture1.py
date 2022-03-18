from selenium import webdriver




link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nНачало работы браузера 1 ..")
        self.browser = webdriver.Chrome(r'C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')

    @classmethod
    def teardown_class(self):
        print("Окончание работы браузера 1 ..")
        self.browser.quit()



    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("Начало работы браузера 2..")
        self.browser = webdriver.Chrome(r'C:\\Users\\user\\PycharmProjects\data_test\\chromedriver.exe')

    def teardown_method(self):
        print("Завршение работы браузера 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")