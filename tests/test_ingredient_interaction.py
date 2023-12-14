import time

from pages.main_page import MainPage


class TestIngredientInteraction:
    def test_detail_form_of_ingredients(self, logged_user):
        main = MainPage(logged_user)
        main.open_detail_form_of_bun()

        assert main.detail_form_is_active() is True, "Детальная форма не открылась"

        main.close_detail_form()

        assert main.detail_form_is_active() is False, "Детальная форма не закрылась"

"""
    def test_offer_with_one_ingredient(self, logged_user):
        main = MainPage(logged_user)
        main.move_bun_in_basket()
        time.sleep(2)

"""