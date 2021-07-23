from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationForm


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Не соответсвует url страницы логина"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы авторизации"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Нет формы регистрации"

    def register_new_user(self, email, password):
        self.browser.find_element(*RegistrationForm.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*RegistrationForm.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*RegistrationForm.PASSWORD_REINPUT).send_keys(password)
        self.browser.find_element(*RegistrationForm.BUTTON).click()


