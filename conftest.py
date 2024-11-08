import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")  # Открытие окна браузера на весь экран
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()