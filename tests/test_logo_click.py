import pytest
import allure
from pages.home_page import HomePage
from data_test.data import Urls

@allure.feature('Навигация по логотипам')
class TestNavigation:
    @allure.title('Переход на главную страницу по клику на логотип Самоката')
    def test_samokat_logo_navigation(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()

        home_page.click_samokat_logo()
        current_url = home_page.get_current_url()
        assert current_url == Urls.BASE_URL, \
            f"Неверный URL после клика на логотип Самоката: {current_url}"

    @allure.title('Переход в Дзен по клику на логотип Яндекса')
    def test_yandex_logo_navigation(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()

        main_window = home_page.get_current_window_handle()
        home_page.click_yandex_logo()
        home_page.wait_for_new_window_opened(main_window)
        new_window = home_page.get_new_window_handle(main_window)
        home_page.switch_to_window(new_window)
        home_page.wait_for_url_contains("dzen.ru")

        current_url = home_page.get_current_url()
        assert "dzen.ru" in current_url, \
            f"Неверный URL после клика на логотип Яндекса: {current_url}"
