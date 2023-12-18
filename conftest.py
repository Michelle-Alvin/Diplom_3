import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage


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
    main = MainPage(driver)
    main.open("https://stellarburgers.nomoreparties.site/")
    main.sign_in_login_page()
    login = LoginPage(driver)
    login.fill_email_password_and_login_button()

    return driver
