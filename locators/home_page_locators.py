from selenium.webdriver.common.by import By

class HomePageLocators:
    # Локаторы для вопросов - исправленные
    QUESTION_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and @hidden='false']")
    
    # Локаторы для кнопок заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[2]")
    
    # Локаторы логотипов
    SAMOKAT_LOGO = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")
    
    # Локатор для куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    # Локатор заголовка страницы
    PAGE_TITLE = (By.XPATH, "//h1[text()='Самокат ']")
