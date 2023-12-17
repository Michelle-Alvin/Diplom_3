import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


@pytest.fixture(scope='function', params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def logged_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.LOGIN_MAIN_PAGE).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE))

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("lukinarseniy001@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    return driver
