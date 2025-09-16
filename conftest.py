import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from data_test.data import Urls

@pytest.fixture
def driver():
    service = FirefoxService()
    drv = webdriver.Firefox(service=service)
    drv.get(Urls.BASE_URL)
    yield drv
    drv.quit()