from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # Заголовок страницы "Восстановление пароля"
    FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")

    # Поле ввода "Email"
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")

    # Кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # Поле ввода пароля
    NEW_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")

    # Переключатель отображения пароля
    DISPLAY_PASSWORD = (By.XPATH, "//div[contains(@class, 'input__icon')]")

    # Активная рамка поля пароль
    PASSWORD_INPUT_STATUS_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
