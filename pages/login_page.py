from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.send_text(*LoginPageLocators.REGISTER_EMAIL_INPUT, email)
        self.send_text(*LoginPageLocators.REGISTER_PASS_INPUT, password)
        self.send_text(*LoginPageLocators.REGISTER_PASS_CONFIRM, password)
        self.element_click(*LoginPageLocators.REGISTER_BUTTON)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, 'URL doesn\'t contain "login" substring'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not presented on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Registration form is not presented on the page'
