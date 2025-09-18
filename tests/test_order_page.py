import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data_test.data import TestData
from locators.home_page_locators import HomePageLocators

@allure.feature('Заказ самоката')
class TestOrder:
    @pytest.mark.parametrize(
        'order_data,order_button_locator',
        [
            (order_data, HomePageLocators.ORDER_BUTTON_HEADER)
            for order_data in TestData.ORDER_DATA_SETS
        ] +
        [
            (order_data, HomePageLocators.ORDER_BUTTON_FOOTER)
            for order_data in TestData.ORDER_DATA_SETS
        ]
    )
    def test_order_scooter_positive_flow(self, driver, order_data, order_button_locator):
        """Позитивный сценарий заказа самоката с выбором кнопки"""
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()

        # Кликаем по нужной кнопке заказа (метод HomePage сам ищет элемент по локатору)
        home_page.click_order_button(order_button_locator)

        # Переход на страницу заказа и заполнение первой страницы
        order_page = OrderPage(driver)
        order_page.fill_first_page(
            order_data['name'],
            order_data['last_name'],
            order_data['address'],
            order_data['metro_station'],
            order_data['phone']
        )

        # Заполнение второй страницы заказа
        order_page.fill_second_page(
            order_data['delivery_date'],
            order_data['rental_period'],
            order_data['color'],
            order_data['comment']
        )

        # Подтверждение заказа
        order_page.confirm_order()

        # Проверка успешного сообщения (методы OrderPage полностью инкапсулируют логику)
        assert order_page.is_success_message_displayed(), \
            "Сообщение об успешном заказе не отображается"
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message, \
            f"Неверное сообщение об успехе: {success_message}"