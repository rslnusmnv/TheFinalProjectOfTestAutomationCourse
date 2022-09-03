from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Link does not contain login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.enter_text(*LoginPageLocators.REGISTRATION_EMAIL_FIELD, email)
        self.enter_text(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, password)
        self.enter_text(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD, password)
        self.click_on_the_button(*LoginPageLocators.REGISTER_BUTTON)

