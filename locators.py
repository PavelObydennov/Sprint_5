from selenium.webdriver.common.by import By

class Locators:
    # Регистрация
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Ссылка на страницу регистрации
    REGISTER_NAME_FIELD = (By.ID, "name")  # Поле ввода имени
    REGISTER_EMAIL_FIELD = (By.ID, "email")  # Поле ввода email
    REGISTER_PASSWORD_FIELD = (By.ID, "password")  # Поле ввода пароля
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка для подтверждения регистрации
    INVALID_PASSWORD_ERROR = (By.CLASS_NAME, "error-message")  # Сообщение об ошибке при некорректном пароле

    # Вход
    MAIN_LOGIN_BUTTON = (By.LINK_TEXT, "Войти в аккаунт")  # Кнопка "Войти в аккаунт" на главной
    LOGIN_EMAIL_FIELD = (By.ID, "login-email")  # Поле ввода email для входа
    LOGIN_PASSWORD_FIELD = (By.ID, "login-password")  # Поле ввода пароля для входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка для подтверждения входа

    # Личный кабинет
    PROFILE_BUTTON = (By.LINK_TEXT, "Личный кабинет")  # Переход в личный кабинет
    PERSONAL_CABINET_HEADER = (By.TAG_NAME, "h1")  # Заголовок "Личный кабинет"
    LOGIN_BUTTON = (By.LINK_TEXT, "Войти")  # Кнопка "Войти" в форме входа

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")  # Переход к конструктору
    SECTION_BUNS = (By.XPATH, "//span[text()='Булки']")  # Таб "Булки"
    SECTION_SAUCES = (By.XPATH, "//span[text()='Соусы']")  # Таб "Соусы"
    SECTION_FILLINGS = (By.XPATH, "//span[text()='Начинки']")  # Таб "Начинки"
    BUNS_SECTION_HEADER = (By.XPATH, "//h2[text()='Булки']")  # Заголовок раздела "Булки"
    SAUCES_SECTION_HEADER = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок раздела "Соусы"
    FILLINGS_SECTION_HEADER = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок раздела "Начинки"

    # Логотип
    LOGO_BUTTON = (By.CLASS_NAME, "logo")  # Кнопка логотипа для перехода на главную

    # Выйти из аккаунта
    LOGOUT_BUTTON = (By.LINK_TEXT, "Выйти")  # Кнопка "Выйти" в личном кабинете