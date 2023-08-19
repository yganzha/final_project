from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators

# from webdriver-manager.chrome import ChromeDriverManager

link = "http://selenium1py.pythonanywhere.com/"


# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
#
#
# def test_guest_should_see_login_link(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()


def test_should_be_login_url(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_url = page.getUrl()
    page.should_be_login_url(page_url)

# def should_be_login_form(self):
#         # реализуйте проверку, что есть форма логина
#     assert True
#
# def should_be_register_form(self):
#         # реализуйте проверку, что есть форма регистрации на странице
#     assert True
