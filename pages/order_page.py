from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.input_text(self.locators.NAME_INPUT, name)
        self.input_text(self.locators.LAST_NAME_INPUT, last_name)
        self.input_text(self.locators.ADDRESS_INPUT, address)
    
    # Выбор станции метро
        self.click_element(self.locators.METRO_STATION_INPUT)
    
    # Используем более надежный локатор
        metro_option = (By.XPATH, f"//div[contains(@class, 'select-search__row')]//*[contains(text(), '{metro_station}')]")
        self.click_element(metro_option)
    
        self.input_text(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)
    def fill_second_page(self, delivery_date, rental_period, color, comment):
        # Заполнение даты доставки
        self.input_text(self.locators.DELIVERY_DATE_INPUT, delivery_date)
        
        # Выбор периода аренды
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        period_option = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']")
        self.click_element(period_option)
        
        # Выбор цвета
        if color == "black":
            self.click_element(self.locators.BLACK_COLOR_CHECKBOX)
        elif color == "grey":
            self.click_element(self.locators.GREY_COLOR_CHECKBOX)
        
        # Комментарий
        self.input_text(self.locators.COMMENT_INPUT, comment)
        
        # Заказ
        self.click_element(self.locators.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.locators.SUCCESS_MESSAGE)

    def is_success_message_displayed(self):
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE)

    def is_order_page_displayed(self):
        return self.is_element_visible(self.locators.ORDER_PAGE_TITLE)

    def get_error_messages(self):
        error_elements = self.find_elements(self.locators.ERROR_MESSAGE)
        return [error.text for error in error_elements]