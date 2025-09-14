import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_test.data import Urls
import allure
from pages.home_page import HomePage

@pytest.fixture
def driver():
    service = FirefoxService()
    drv = webdriver.Firefox(service=service)
    drv.get(Urls.BASE_URL)
    yield drv
    drv.quit()

@allure.feature('Навигация по логотипам')
class TestNavigation:
    def test_samokat_logo_navigation(self, driver):
        with allure.step('Открыть главную страницу'):
            home_page = HomePage(driver)
            home_page.accept_cookies()
        
        with allure.step('Нажать на логотип Самоката'):
            home_page.click_samokat_logo()
        
        with allure.step('Проверить переход на главную страницу'):
            current_url = home_page.get_current_url()
            assert current_url == "https://qa-scooter.praktikum-services.ru/", \
                f"Неверный URL после клика на логотип Самоката: {current_url}"

    def test_yandex_logo_navigation(self, driver):
        with allure.step('Открыть главную страницу'):
            home_page = HomePage(driver)
            home_page.accept_cookies()
        
        with allure.step('Запомнить текущее окно'):
            main_window = driver.current_window_handle
        
        with allure.step('Нажать на логотип Яндекса'):
            home_page.click_yandex_logo()
        
        with allure.step('Переключиться на новое окно'):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            windows = driver.window_handles
            new_window = [window for window in windows if window != main_window][0]
            driver.switch_to.window(new_window)
        
        with allure.step('Проверить переход на Дзен'):
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
            current_url = driver.current_url
            assert "dzen.ru" in current_url, \
                f"Неверный URL после клика на логотип Яндекса: {current_url}"
