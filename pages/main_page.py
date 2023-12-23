import time

import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Переходим на страницу авторизации')
    def sign_in_login_page(self):
        self.click(MainPageLocators.LOGIN_MAIN_PAGE)

    @allure.step('Переходим в профиль пользователя')
    def go_to_my_profile(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Переходим в ленту заказов')
    def go_to_orders_list(self):
        self.click(MainPageLocators.FEED_LINK)
        return self.is_active(MainPageLocators.FEED_TITLE)

    @allure.step('Переходим в конструктор')
    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)
        return self.is_active(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Открываем детальную форму флюоресцентной булки')
    def open_detail_form_of_bun(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)

    @allure.step('Проверяем отображение окна детальной информации ингредиента')
    def detail_form_is_active(self):
        return self.is_active(MainPageLocators.CROSS_DETAIL_FORM)

    @allure.step('Закрываем окно детальной информации')
    def close_detail_form(self):
        self.click(MainPageLocators.CROSS_DETAIL_FORM)

    @allure.step('Переносим булку в корзину')
    def move_bun_in_basket(self):
        self.move_from_to(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.BURGER_BASKET)

    @allure.step('Проверяем счетчик булок в заказе')
    def get_count_of_buns(self):
        return self.get_text(MainPageLocators.COUNT_FLUORESCENT_BUN)

    @allure.step('Жмем "Оформить заказ" и сохраняем номер заказа')
    def accept_order(self):
        self.click(MainPageLocators.MAKE_ORDER)
        return self.get_order_number(MainPageLocators.ORDER_NUMBER)

    @allure.step('Открываем детальный просмотр первого заказа в ленте заказов')
    def open_detail_form_first_order_in_feed(self):
        self.click(MainPageLocators.FIRST_ORDER_IN_FEED)
        return self.is_active(MainPageLocators.DETAIL_FORM_ORDER)

    @allure.step('Получаем значение заказов за все время')
    def count_orders_for_all_time(self):
        return self.get_text(MainPageLocators.COUNT_FOR_ALL_TIME)

    @allure.step('Получаем значение заказов за день')
    def count_orders_in_a_day(self):
        return self.get_text(MainPageLocators.COUNT_IN_A_DAY)

    @allure.step('Проверяем отображение заказа в блоке "В работе"')
    def search_order_in_progress_list(self):
        return self.is_active(MainPageLocators.ORDER_IN_PROGRESS)
