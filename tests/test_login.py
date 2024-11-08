import pytest
from locators import Locators
from urls import Urls
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_login_via_main_button(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_EMAIL_FIELD)
        ).send_keys("pavelpavlov@mail.com")

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_FIELD)
        ).send_keys("123456789!!!")

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.LOGIN_SUBMIT_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.PERSONAL_CABINET_HEADER)
        )

    def test_login_via_profile_button(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.PROFILE_BUTTON)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_EMAIL_FIELD)
        ).send_keys("pavelpavlov@mail.com")

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_FIELD)
        ).send_keys("123456789!!!")

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.LOGIN_SUBMIT_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.PERSONAL_CABINET_HEADER)
        )