from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


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
        actions = ActionChains(self.driver)
        actions.click_and_hold(MainPageLocators.FLUORESCENT_BUN).move_to_element(MainPageLocators.BURGER_BASKET).release().perform()



