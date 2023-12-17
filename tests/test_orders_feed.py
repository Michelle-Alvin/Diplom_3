import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestOrdersFeed:
    @allure.title("Детальная форма заказа в ленте заказов")
    def test_detail_of_order(self, driver):
        main = MainPage(driver)
        main.open("https://stellarburgers.nomoreparties.site/")
        main.go_to_orders_list()
        res = main.open_detail_form_first_order_in_feed()

        assert res is True, "Детальная форма заказов не открылась"

    @allure.title("Отображение заказа в Ленте заказов и истории профиля")
    def test_user_orders_displayed_in_order_feed(self, logged_user):
        main = MainPage(logged_user)
        main.move_bun_in_basket()
        order_number = main.accept_order()
        main.close_detail_form()
        main.go_to_orders_list()

        assert main.search_order(order_number) is True, "Созданная заявка не найдена в ленте заказов"

        main.go_to_my_profile()
        login = LoginPage(logged_user)
        login.go_to_order_history()

        assert login.search_order(order_number) is True, "Созданная заявка не найдена в истории заказов"

    @allure.title("Проверка корректности счетчика заказов за все время")
    def test_order_count_for_all_time(self, logged_user):
        main = MainPage(logged_user)
        # Идем в ленту заказов и берем текущее значение заказов за все время
        main.go_to_orders_list()
        count = main.count_orders_for_all_time()

        # Идем в конструктор и делаем новый заказ
        main.go_to_constructor()
        main.move_bun_in_basket()
        main.accept_order()
        main.close_detail_form()

        # Возвращаемся в ленту и проверяем новое значение
        main.go_to_orders_list()

        assert main.count_orders_for_all_time() > count, "счетчик заказов за все время не изменился"

    @allure.title("Проверка корректности счетчика заказов за день")
    def test_order_count_in_a_day(self, logged_user):
        main = MainPage(logged_user)
        # Идем в ленту заказов и берем текущее значение заказов за день
        main.go_to_orders_list()
        count = main.count_orders_in_a_day()

        # Идем в конструктор и делаем новый заказ
        main.go_to_constructor()
        main.move_bun_in_basket()
        main.accept_order()
        main.close_detail_form()

        # Возвращаемся в ленту и проверяем новое значение
        main.go_to_orders_list()

        assert main.count_orders_in_a_day() > count, "счетчик заказов за день не изменился"

    @allure.title('Отображение нового заказа в блоке "В работе"')
    def test_order_in_progress(self, logged_user):
        main = MainPage(logged_user)
        main.move_bun_in_basket()
        main.accept_order()
        main.close_detail_form()
        main.go_to_orders_list()

        assert main.search_order_in_progress_list() is True
