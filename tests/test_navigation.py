from locators import Locators
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigation:
    def test_navigation_to_profile(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.PROFILE_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )

    def test_navigation_to_constructor_from_profile(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.PROFILE_BUTTON)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.BUNS_SECTION_HEADER)
        )

    def test_navigation_to_home_via_logo(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.PROFILE_BUTTON)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.BUNS_SECTION_HEADER)
        )

    def test_logout(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.PROFILE_BUTTON)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_EMAIL_FIELD)
        ).send_keys("pavelpavlov@mail.com")

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_FIELD)
        ).send_keys("password123")

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.LOGIN_SUBMIT_BUTTON)
        ).click()

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )