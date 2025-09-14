import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from data_test.data import Urls

@pytest.fixture
def driver():
    service = FirefoxService()  # или FirefoxService(executable_path="C:\\path\\to\\geckodriver.exe")
    drv = webdriver.Firefox(service=service)
    drv.get(Urls.BASE_URL)
    yield drv
    drv.quit()

import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data_test.data import TestData

@allure.feature('Заказ самоката')
class TestOrder:
    @pytest.mark.parametrize('order_data_sets', TestData.ORDER_DATA_SETS)
    @pytest.mark.parametrize('button_position', ['top', 'bottom'])
    def test_order_scooter_positive_flow(self, driver, order_data_sets, button_position):
        with allure.step('Открыть главную страницу'):
            home_page = HomePage(driver)
            home_page.accept_cookies()
        
        with allure.step(f'Нажать кнопку "Заказать" ({button_position})'):
            if button_position == 'top':
                home_page.click_order_button_top()
            else:
                home_page.click_order_button_bottom()
        
        with allure.step('Заполнить первую страницу заказа'):
            order_page = OrderPage(driver)
            order_page.fill_first_page(
                order_data_sets['name'],
                order_data_sets['last_name'],
                order_data_sets['address'],
                order_data_sets['metro_station'],
                order_data_sets['phone']
            )
        
        with allure.step('Заполнить вторую страницу заказа'):
            order_page.fill_second_page(
                order_data_sets['delivery_date'],
                order_data_sets['rental_period'],
                order_data_sets['color'],
                order_data_sets['comment']
            )
        
        with allure.step('Подтвердить заказ'):
            order_page.confirm_order()
        
        with allure.step('Проверить сообщение об успешном заказе'):
            assert order_page.is_success_message_displayed(), \
                "Сообщение об успешном заказе не отображается"
            
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Неверное сообщение об успехе: {success_message}"
