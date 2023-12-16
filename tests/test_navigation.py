import allure

from pages.main_page import MainPage


class TestNavigation:
    @allure.title("Навигация: переходы в Ленту заказов и Конструктор")
    def test_navigation(self, driver):
        main = MainPage(driver)
        main.open("https://stellarburgers.nomoreparties.site/")
        res = main.go_to_orders_list()

        assert res == "Лента заказов", "Ошибка при переходе в ленту заказов"

        res = main.go_to_constructor()

        assert res == "Соберите бургер", "Ошибка перехода в конструктор заказа"
