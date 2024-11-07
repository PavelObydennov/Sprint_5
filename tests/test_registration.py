from locators import Locators
from helpers import generate_unique_email
from urls import Urls
from fixtures import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.REGISTER_NAME_FIELD)
        ).send_keys("Павел")

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.REGISTER_EMAIL_FIELD)
        ).send_keys(generate_unique_email())

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.REGISTER_PASSWORD_FIELD)
        ).send_keys("123456789!!!")  # Фиксированный пароль

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.REGISTER_SUBMIT_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.PERSONAL_CABINET_HEADER)
        )

    def test_invalid_password_registration(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.REGISTER_NAME_FIELD)
        ).send_keys("Павел")

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.REGISTER_EMAIL_FIELD)
        ).send_keys(generate_unique_email())

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.REGISTER_PASSWORD_FIELD)
        ).send_keys("123")  # Некорректный короткий пароль

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.REGISTER_SUBMIT_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.INVALID_PASSWORD_ERROR)
        )