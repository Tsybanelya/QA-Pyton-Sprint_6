from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step("Открываем страницу заказа")
    def open(self):
        self.driver.get(self.base_url + "order")  # если страница заказа по /order, можно явно прописать

    @allure.step("Заполняем первую страницу заказа: имя={name}, фамилия={last_name}, адрес={address}, метро={metro_station}, телефон={phone}")
    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.input_text(self.locators.NAME_INPUT, name)
        self.input_text(self.locators.LAST_NAME_INPUT, last_name)
        self.input_text(self.locators.ADDRESS_INPUT, address)
        self.click_element(self.locators.METRO_STATION_INPUT)
        # Надежный выбор станции метро через BasePage
        metro_option = (By.XPATH, f"//div[contains(@class, 'select-search__row')]//div[contains(text(), '{metro_station}')]")
        self.click_element(metro_option)
        self.input_text(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполняем вторую страницу заказа: дата={delivery_date}, период={rental_period}, цвет={color}, коммент={comment}")
    def fill_second_page(self, delivery_date, rental_period, color, comment):
        self.input_text(self.locators.DELIVERY_DATE_INPUT, delivery_date)
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        period_option = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']")
        self.click_element(period_option)
        # Выбор цвета
        if color == "black":
            self.click_element(self.locators.BLACK_COLOR_CHECKBOX)
        elif color == "grey":
            self.click_element(self.locators.GREY_COLOR_CHECKBOX)
        self.input_text(self.locators.COMMENT_INPUT, comment)
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step("Подтверждаем оформление заказа")
    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получаем текст сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text(self.locators.SUCCESS_MESSAGE)

    @allure.step("Проверяем отображение окна успешного заказа")
    def is_success_message_displayed(self):
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE)

    @allure.step("Проверяем, что страница заказа открыта")
    def is_order_page_displayed(self):
        return self.is_element_visible(self.locators.ORDER_PAGE_TITLE)

    @allure.step("Получаем ошибки валидации формы")
    def get_error_messages(self):
        error_elements = self.find_elements(self.locators.ERROR_MESSAGES)
        return [error.text for error in error_elements]