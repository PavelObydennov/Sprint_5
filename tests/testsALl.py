import pytest
import time
from selenium import webdriver
from locators import Locators


def test_successful_registration(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.REGISTER_LINK).click()

    driver.find_element(*Locators.REGISTER_NAME_FIELD).send_keys("Павел")
    driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys("pavelpavlov@mail.com")
    driver.find_element(*Locators.REGISTER_PASSWORD_FIELD).send_keys("123456789!!!")
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()

    # Проверка успешной регистрации
    assert "Личный кабинет" in driver.page_source


def test_invalid_password_registration(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.REGISTER_LINK).click()

    driver.find_element(*Locators.REGISTER_NAME_FIELD).send_keys("Paveltest")
    driver.find_element(*Locators.REGISTER_EMAIL_FIELD).send_keys("pavelpavlov@mail.com")
    driver.find_element(*Locators.REGISTER_PASSWORD_FIELD).send_keys("12")
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()

    # Проверка ошибки некорректного пароля
    assert "Некорректный пароль" in driver.page_source


def test_login_via_main_button(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("pavelpavlov@mail.com")
    driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("123456789!!!")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Проверка успешного входа
    assert "Личный кабинет" in driver.page_source


def test_login_via_profile_button(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.PROFILE_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("pavelpavlov@mail.com")
    driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("123456789!!!")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Проверка успешного входа
    assert "Личный кабинет" in driver.page_source


def test_login_via_registration_form(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.REGISTER_LINK).click()
    driver.find_element(*Locators.REGISTER_LOGIN_LINK).click()

    driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("pavelpavlov@mail.com")
    driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("123456789!!!")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Проверка успешного входа
    assert "Личный кабинет" in driver.page_source


def test_login_via_password_recovery_form(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.PASSWORD_RECOVERY_LINK).click()
    driver.find_element(*Locators.REGISTER_LOGIN_LINK).click()

    driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("pavelpavlov@mail.com")
    driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("123456789!!!")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Проверка успешного входа
    assert "Личный кабинет" in driver.page_source


def test_navigation_to_profile(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.PROFILE_BUTTON).click()

    # Проверка перехода в личный кабинет
    assert "Войти" in driver.page_source


def test_navigation_to_constructor(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.PROFILE_BUTTON).click()
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    # Проверка перехода к конструктору
    assert "Соберите бургер" in driver.page_source


def test_navigation_to_home_via_logo(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.PROFILE_BUTTON).click()
    driver.find_element(*Locators.LOGO_BUTTON).click()

    # Проверка перехода на главную страницу по логотипу
    assert "Соберите бургер" in driver.page_source


def test_logout(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.PROFILE_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL_FIELD).send_keys("pavelpavlov@mail.com")
    driver.find_element(*Locators.LOGIN_PASSWORD_FIELD).send_keys("123456789!!!")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    driver.find_element(*Locators.LOGOUT_BUTTON).click()

    # Проверка выхода из системы
    assert "Войти в аккаунт" in driver.page_source


def test_constructor_sections(setup):
    driver = setup
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*Locators.SECTION_BUNS).click()
    assert "Булки" in driver.page_source

    driver.find_element(*Locators.SECTION_SAUCES).click()
    assert "Соусы" in driver.page_source

    driver.find_element(*Locators.SECTION_FILLINGS).click()
    assert "Начинки" in driver.page_source