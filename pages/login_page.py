from .base_page import BasePage



class LoginPage(BasePage):
    def should_be_login_url(self, page_url):
        assert "login" in page_url, "url is incorrect"

    # def should_be_login_page(self):
        # self.should_be_login_url()
        # self.should_be_login_form()
        # self.should_be_register_form()