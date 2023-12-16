import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def sign_in_login_page(self):
        self.click(MainPageLocators.LOGIN_MAIN_PAGE)

    def go_to_my_profile(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT)

    def go_to_orders_list(self):
        self.click(MainPageLocators.FEED_LINK)
        return self.get_text(MainPageLocators.FEED_TITLE)

    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)
        return self.get_text(MainPageLocators.CONSTRUCTOR_TITLE)

    def open_detail_form_of_bun(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)

    def detail_form_is_active(self):
        return self.is_active(MainPageLocators.CROSS_DETAIL_FORM)

    def close_detail_form(self):
        self.click(MainPageLocators.CROSS_DETAIL_FORM)

    def move_bun_in_basket(self):
        fluorescence_bun = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            MainPageLocators.FLUORESCENT_BUN))
        burger_basket = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            MainPageLocators.BURGER_BASKET))

        actions = ActionChains(self.driver)
        actions.click_and_hold(fluorescence_bun) \
            .move_to_element(burger_basket).release().perform()

    def get_count_of_buns(self):
        return self.get_text(MainPageLocators.COUNT_FLUORESCENT_BUN)

    def accept_order(self):
        self.click(MainPageLocators.MAKE_ORDER)
        time.sleep(2)
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    def open_detail_form_first_order_in_feed(self):
        self.click(MainPageLocators.FIRST_ORDER_IN_FEED)
        return self.is_active(MainPageLocators.DETAIL_FORM_ORDER)

    def count_orders_for_all_time(self):
        return self.get_text(MainPageLocators.COUNT_FOR_ALL_TIME)

    def count_orders_in_a_day(self):
        return self.get_text(MainPageLocators.COUNT_IN_A_DAY)

    def search_order_in_progress_list(self, number):
        return self.is_active(MainPageLocators.order_in_progress(number))
