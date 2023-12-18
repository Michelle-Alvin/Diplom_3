import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Нажимаем "Восстановить пароль"')
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    @allure.step('Проверяем отображение данных профиля')
    def check_profile_list_active(self):
        return self.is_active(LoginPageLocators.PROFILE_LIST)

    @allure.step('Переходим в историю заказов')
    def go_to_order_history(self):
        self.click(LoginPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверяем отображение вкладки истории заказов')
    def check_order_history_active(self):
        return self.is_active(LoginPageLocators.ORDER_HISTORY)

    @allure.step('Выходим из профиля по кнопки "Выход"')
    def logout_from_profile(self):
        self.click(LoginPageLocators.EXIT_BUTTON)

    @allure.step('Проверяем открытую главную страницу (Конструктор)')
    def check_login_page(self):
        return self.is_active(LoginPageLocators.LOGIN_TITLE)

    @allure.step('Заполняем данные для входа в тестовую запись и жмем кнопку входа')
    def fill_email_password_and_login_button(self):
        self.fill_input(LoginPageLocators.EMAIL_INPUT, "lukinarseniy001@yandex.ru")
        self.fill_input(LoginPageLocators.PASSWORD_INPUT, "123456")
        self.click(LoginPageLocators.LOGIN_BUTTON)
