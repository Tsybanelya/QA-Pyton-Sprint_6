from selenium.webdriver.common.by import By

class HomePageLocators:
    # Локаторы для вопросов
    QUESTION_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]")
    
    # Кнопка "Заказать" в хедере
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, ".Header_Nav__AGCXC .Button_Button__ra12g")
    # Кнопка "Заказать" внизу страницы  
    ORDER_BUTTON_FOOTER = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm > button")

    # Логотип Самоката 
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@href, '/')]")
    # Логотип Яндекса 
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'yandex.ru')]")
    
    # Кнопка согласия с куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    # Заголовок страницы — ищем по тексту, без абсолютного пути
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Самокат')]")