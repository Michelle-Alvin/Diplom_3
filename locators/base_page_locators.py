from selenium.webdriver.common.by import By


class BasePageLocators:
    @staticmethod
    def order_number(order_number):
        return By.XPATH, f"//p[contains(text(), '{order_number}')]"
