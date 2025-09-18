from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая страница заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTIONS = (By.XPATH, "//div[contains(@class, 'select-search__row')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Далее']")

    # Вторая страница заказа
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-root')]")
    RENTAL_PERIOD_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")

    # Цвет самоката (лучше по id, если он уникален)
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and normalize-space(text())='Заказать']")
    
    # Подтверждение заказа
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    
    # Валидация и ошибки
    ERROR_MESSAGES = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage')]")
    
    # Заголовок страницы заказа
    ORDER_PAGE_TITLE = (By.XPATH, "//div[contains(@class, 'Order_Header')]")