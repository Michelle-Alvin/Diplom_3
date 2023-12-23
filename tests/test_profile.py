import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestProfile:
    @allure.title("Проверка информации в профиле клиента")
    def test_profile_info_tab(self, logged_user):
        main = MainPage(logged_user)
        main.go_to_my_profile()
        profile = LoginPage(logged_user)

        assert profile.check_profile_list_active(), "Раздел профиль не отображен"

    @allure.title("Проверка вкладки истории заказов в профиле клиента")
    def test_profile_history_tab(self, logged_user):
        main = MainPage(logged_user)
        main.go_to_my_profile()
        profile = LoginPage(logged_user)
        profile.go_to_order_history()

        assert profile.check_order_history_active(), "Список заказов не отображен"

    @allure.title("Проверка логаута")
    def test_profile_exit(self, logged_user):
        main = MainPage(logged_user)
        main.go_to_my_profile()
        profile = LoginPage(logged_user)
        profile.logout_from_profile()

        assert profile.check_login_page(), "Выход из аккаунта не выполнен"
