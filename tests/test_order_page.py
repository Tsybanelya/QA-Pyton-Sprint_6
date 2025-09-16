import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data_test.data import TestData

@allure.feature('Заказ самоката')
class TestOrder:

    # Формируем пары (order_data, button_position) для параметризации
    @pytest.mark.parametrize(
        'order_data,button_position',
        [
            (order_data, button_position) 
            for order_data in TestData.ORDER_DATA_SETS
            for button_position in ['top', 'bottom']
        ]
    )
    def test_order_scooter_positive_flow(self, driver, order_data, button_position):
        """Позитивный сценарий заказа самоката с любой позиции кнопки"""
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()

        # Клик по кнопке заказа через PageObject, без условного блока
        if button_position == 'top':
            home_page.click_order_button_top()
        else:
            home_page.click_order_button_bottom()

        # Заполняем первую страницу заказа
        order_page = OrderPage(driver)
        order_page.fill_first_page(
            order_data['name'],
            order_data['last_name'],
            order_data['address'],
            order_data['metro_station'],
            order_data['phone']
        )

        # Заполняем вторую страницу заказа
        order_page.fill_second_page(
            order_data['delivery_date'],
            order_data['rental_period'],
            order_data['color'],
            order_data['comment']
        )

        # Подтверждаем заказ
        order_page.confirm_order()

        # Проверяем сообщение об успешном заказе
        assert order_page.is_success_message_displayed(), \
            "Сообщение об успешном заказе не отображается"
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message, \
            f"Неверное сообщение об успехе: {success_message}"