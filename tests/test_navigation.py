import allure

from pages.main_page import MainPage


class TestNavigation:
    @allure.title("Навигация: переходы в Ленту заказов")
    def test_navigation(self, driver):
        main = MainPage(driver)
        main.open("https://stellarburgers.nomoreparties.site/")

        assert main.go_to_orders_list() is True, "Ошибка при переходе в ленту заказов"

    @allure.title("Навигация: переход в Конструктор")
    def test_navigation_constructor(self, driver):
        main = MainPage(driver)
        main.open("https://stellarburgers.nomoreparties.site/feed")

        assert main.go_to_constructor() is True, "Ошибка перехода в конструктор заказа"
