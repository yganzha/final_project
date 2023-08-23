from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self, page_url):
        self.should_be_login_url(page_url)
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self, page_url):
        assert "login" in page_url, "No login in url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No Login form"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "No Registration form"


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
