import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestForgotPassword:
    @allure.title("Ворк-флоу восстановления пароля")
    def test_input_status_active(self, driver):
        main = MainPage(driver)
        main.open('https://stellarburgers.nomoreparties.site/')
        main.sign_in_login_page()
        login = LoginPage(driver)
        login.click_forgot_password()
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.fill_email()
        forgot_password.click_restore_button()
        forgot_password.fill_password()
        forgot_password.click_display_password()

        assert forgot_password.password_field_is_active() is True, "Поле ввода пароля не подсветилось"
