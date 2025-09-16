from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure

class HomePage(BasePage):
    @allure.step("Инициализация HomePage")
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    @allure.step("Открываем главную страницу")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Принимаем cookies")
    def accept_cookies(self):
        self.click_element(self.locators.COOKIE_BUTTON)

    @allure.step("Кликаем по вопросу с индексом: {index}")
    def click_question(self, index):
        questions = self.find_elements(self.locators.QUESTION_LOCATOR)
        if index < len(questions):
            questions[index].click()

    @allure.step("Получаем текст открытого ответа")
    def get_answer_text(self):
        answer = self.wait_for_element_visible(self.locators.ANSWER_LOCATOR)
        return answer.text

    @allure.step("Кликаем по верхней кнопке 'Заказать'")
    def click_order_button_top(self):
        buttons = self.find_elements(self.locators.ORDER_BUTTONS)
        if buttons:
            buttons[0].click()

    @allure.step("Кликаем по нижней кнопке 'Заказать'")
    def click_order_button_bottom(self):
        # Скролл может остаться, если он необходим для доступности кнопки
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        buttons = self.find_elements(self.locators.ORDER_BUTTONS)
        if len(buttons) > 1:
            buttons[1].click()

    @allure.step("Кликаем по логотипу Самоката")
    def click_samokat_logo(self):
        self.click_element(self.locators.SAMOKAT_LOGO)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверяем, что главная страница отображается")
    def is_home_page_displayed(self):
        return self.is_element_visible(self.locators.PAGE_TITLE)
    @allure.step("Ждём, что ответ стал видимым")
    def is_answer_visible(self):
        return self.is_element_visible(self.locators.ANSWER_LOCATOR)

    @allure.step("Ждём, что ответ исчез с экрана")
    def wait_for_answer_disappear(self):
        self.wait_for_element_to_disappear(self.locators.ANSWER_LOCATOR)

    @allure.step("Проверяем, что вопрос с индексом {index} свернут (нет класса active)")
    def is_question_collapsed(self, index):
        questions = self.find_elements(self.locators.QUESTION_LOCATOR)
        accordion_item = questions[index].find_element(
        By.XPATH, "./ancestor::div[contains(@class, 'accordion__item')]"
    )
        return "accordion__item_active" not in accordion_item.get_attribute("class")
