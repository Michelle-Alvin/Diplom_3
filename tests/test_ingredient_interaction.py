import allure

from pages.main_page import MainPage


class TestIngredientInteraction:
    @allure.title("Детальная форма ингредиентов в конструкторе")
    def test_detail_form_of_ingredients(self, logged_user):
        main = MainPage(logged_user)
        main.open_detail_form_of_bun()

        assert main.detail_form_is_active() is True, "Детальная форма не открылась"

        main.close_detail_form()

        assert main.detail_form_is_active() is False, "Детальная форма не закрылась"

    @allure.title("Проверка оформления заказа")
    def test_offer_with_one_ingredient(self, logged_user):
        main = MainPage(logged_user)
        main.move_bun_in_basket()
        count = int(main.get_count_of_buns())

        assert count == 2, "Ингредиент не добавлен"

        order_number = main.accept_order()

        assert order_number, "Окно заказ не открыто"
