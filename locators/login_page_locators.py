from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Заголовок страницы /login
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")

    # Поле ввода "Email"
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")

    # Поле ввода "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Кнопка "Восстановить пароль"
    FORGOT_PASSWORD_BUTTON = (By.LINK_TEXT, 'Восстановить пароль')

    # Таблица данных профиля видимая в активном состоянии
    PROFILE_LIST = (By.XPATH, "//ul[contains(@class, 'Profile_profileList')]")

    # Кнопка истории заказов
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')

    # Список заказов когда активна
    ORDER_HISTORY = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]")

    # Кнопка "Выход"
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
