from selenium.webdriver.common.by import By

# Кнопка "Личный кабинет"
PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

# Кнопка "Зарегистрироваться"
REGISTER_BUTTON = (By.LINK_TEXT, 'Зарегистрироваться')

# Страница регистрации
REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")

# Поле ввода имени на странице регистрации
REGISTER_NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")

# Поле ввода email на странице регистрации
EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")

# Поле ввода email на странице регистрации
PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")

# Кнопка отправки регистрирации
REGISTER_SEND = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

# Страница регистрации
LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")

# Некорректный пароль
INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")

# Кнопка "Войти в аккаунт" на главной странице
LOGIN_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Кнопка "Войти" при авторизации в аккаунте
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Кнопка "Оформить заказ"
CHECKOUT = (By.XPATH, "//button[text()='Оформить заказ']")

# Кнопка "Войти" на странице авторизации
ENTER_BUTTON = (By.XPATH, "//a[text()='Войти']")

# Кнопка "Восстановить пароль"
FORGOT_PASSWORD_BUTTON = (By.LINK_TEXT, 'Восстановить пароль')

# Заголовок страницы восстановления пароля
FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")

# Вкладка "История заказов"
ORDERS_HISTORY = (By.LINK_TEXT, 'История заказов')

# Вкладка "Конструктор"
CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")

# Логотип "Stellar Burgers"
LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

# Кнопка "Выход" из аккаунта
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Активная вкладка конструктора
ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_type_current')]")

# Вкладка "Булки"
BUNS = (By.XPATH, "//span[text()='Булки']")

# Вкладка "Соусы"
SAUSES = (By.XPATH, "//span[text()='Соусы']")

# Вкладка "Начинки"
TOPPINGS = (By.XPATH, "//span[text()='Начинки']")
