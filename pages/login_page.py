from locators import login_page_locators
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    def check_profile_list_active(self):
        return self.is_active(LoginPageLocators.PROFILE_LIST)

    def go_to_order_history(self):
        self.click(LoginPageLocators.ORDER_HISTORY_BUTTON)

    def check_order_history_active(self):
        return self.is_active(LoginPageLocators.ORDER_HISTORY)

    def logout_from_profile(self):
        self.click(LoginPageLocators.EXIT_BUTTON)

    def check_login_page(self):
        return self.get_text(LoginPageLocators.LOGIN_TITLE)
