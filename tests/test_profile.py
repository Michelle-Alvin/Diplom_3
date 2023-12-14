from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestProfile:
    def test_profile_tabs(self, logged_user):
        main = MainPage(logged_user)
        main.go_to_my_profile()
        profile = LoginPage(logged_user)

        assert profile.check_profile_list_active(), "Раздел профиль не отображен"

        profile.go_to_order_history()

        assert profile.check_order_history_active(), "Список заказов не отображен"

        profile.logout_from_profile()

        assert profile.check_login_page() == "Вход", "Выход из аккаунта не выполнен"
