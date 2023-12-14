import allure
from selenium.common import NoSuchElementException

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def fill_email(self):
        self.fill_input(ForgotPasswordPageLocators.EMAIL_INPUT, "lukinarseniy001@yandex.ru")

    def click_restore_button(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)

    def fill_password(self):
        self.fill_input(ForgotPasswordPageLocators.NEW_PASSWORD_INPUT, "123asd")

    def click_display_password(self):
        self.click(ForgotPasswordPageLocators.DISPLAY_PASSWORD)

    def password_field_is_active(self):
        return self.is_active(ForgotPasswordPageLocators.PASSWORD_INPUT_STATUS_ACTIVE)
