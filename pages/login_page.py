from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login link is not presented"

        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert 'login' in self.browser.current_url, 'Error: string login is not found'
        # реализуем проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуем проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "register form is not presented"
        # реализуем проверку, что есть форма регистрации на странице

    def register_new_user(self, email, password):
        email_register = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        email_register.send_keys(email)

        password_register = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)
        password_register.send_keys(password)

        repeat_password = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_REGISTER)
        repeat_password.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

