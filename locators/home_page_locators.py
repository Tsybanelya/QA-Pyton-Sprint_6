from selenium.webdriver.common.by import By

class HomePageLocators:
    # Локаторы для вопросов
    QUESTION_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]")
    
    # Локаторы для кнопок заказа (ищем все, выбор в тестах по индексу; оптимально добавить data-атрибуты в разметку)
    ORDER_BUTTONS = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    
    # Логотип Самоката 
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@href, '/')]")
    # Логотип Яндекса 
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'yandex.ru')]")
    
    # Кнопка согласия с куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    # Заголовок страницы — ищем по тексту, без абсолютного пути
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Самокат')]")