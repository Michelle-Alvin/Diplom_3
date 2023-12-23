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
    CROSS_DETAIL_FORM = (
        By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")

    # Флюоресцентная булка в конструкторе
    FLUORESCENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    # Корзина конструктора
    BURGER_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    # Счетчик заказанных булочек
    COUNT_FLUORESCENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']/ancestor::"
                                       "div//p[contains(@class, 'counter_counter__num')]")

    # Кнопка Оформить заказ
    MAKE_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")

    # Открытое окно заказа
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")

    # Открытое окно заказа
    ORDER_CONFIRMATION = (By.XPATH, "//p[text() = 'идентификатор заказа'")

    # Первый элемент в ленте заказов
    FIRST_ORDER_IN_FEED = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]")

    # Детальная форма заказа в ленте заказов
    DETAIL_FORM_ORDER = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")

    # Счетчик заказов за все время
    COUNT_FOR_ALL_TIME = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")

    # Счетчик заказов за день
    COUNT_IN_A_DAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")

    # Номер заказа в списке заказов "В работе"
    ORDER_IN_PROGRESS = (By.XPATH, f"//li[contains(text(), '0')]")
