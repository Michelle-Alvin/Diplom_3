from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

    # Ссылка в ленту заказов
    FEED_LINK = (By.LINK_TEXT, 'Лента Заказов')

    # Заголовок страницы "Лента заказов"
    FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    # Ссылка на конструктор
    CONSTRUCTOR_LINK = (By.LINK_TEXT, 'Конструктор')

    # Заголовок страницы конструктора
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    # Крестик в детальной информации ингредиента
    CROSS_DETAIL_FORM = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")

    # Флюоресцентная булка в конструкторе
    FLUORESCENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    # Корзина конструктора
    BURGER_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

