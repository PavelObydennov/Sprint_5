from locators import Locators
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructorSections:
    def test_constructor_buns_section(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.SECTION_BUNS)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.BUNS_SECTION_HEADER)
        )

    def test_constructor_sauces_section(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.SECTION_SAUCES)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.SAUCES_SECTION_HEADER)
        )

    def test_constructor_fillings_section(self, driver):
        driver.get(Urls.HOME_URL)

        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(Locators.SECTION_FILLINGS)
        ).click()

        assert WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(Locators.FILLINGS_SECTION_HEADER)
        )