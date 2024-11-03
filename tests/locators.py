from selenium.webdriver.common.by import By

class Locators:
    # Главная страница
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PROFILE_BUTTON = (By.LINK_TEXT, 'Личный кабинет')  # Кнопка «Личный кабинет»

    # Страница Логина
    LOGIN_EMAIL_FIELD = (By.NAME, 'email')  # Поле Email для ввода
    LOGIN_PASSWORD_FIELD = (By.NAME, 'password')  # Поле Пароль для ввода
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»

    # Страница Регистрации
    REGISTER_LINK = (By.LINK_TEXT, 'Регистрация')  # Ссылка на регистрацию
    REGISTER_NAME_FIELD = (By.NAME, 'name')  # Поле Имя для ввода
    REGISTER_EMAIL_FIELD = (By.NAME, 'email')  # Поле Email для ввода
    REGISTER_PASSWORD_FIELD = (By.NAME, 'password')  # Поле Пароль для ввода
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка для подачи формы регистрации
    REGISTER_LOGIN_LINK = (By.LINK_TEXT, 'Войти в аккаунт')  # Ссылка как альтернатива после регистрации

    # Страница восстановления пароля
    PASSWORD_RECOVERY_LINK = (By.LINK_TEXT, 'Восстановить пароль')  # Ссылка на восстановление пароля

    # Личный кабинет
    PERSONAL_CABINET_HEADER = (By.XPATH, "//h2[text()='Личный кабинет']")  # Заголовок личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка выхода из личного кабинета

    # Страница конструктора
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок конструктора
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка «Конструктор»
    LOGO_BUTTON = (
    By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")  # Логотип Stellar Burgers для возврата на главную

    # Разделы конструктора
    SECTION_BUNS = (By.XPATH, "//span[text()='Булки']")  # Раздел «Булки»
    SECTION_SAUCES = (By.XPATH, "//span[text()='Соусы']")  # Раздел «Соусы»
    SECTION_FILLINGS = (By.XPATH, "//span[text()='Начинки']")  # Раздел «Начинки»