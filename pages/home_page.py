from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()
        self.driver.get(self.base_url)

    def accept_cookies(self):
        self.click_element(self.locators.COOKIE_BUTTON)

    def click_question(self, index):
        questions = self.find_elements(self.locators.QUESTION_LOCATOR)
        if index < len(questions):
            questions[index].click()

    def get_answer_text(self, index):
        try:
        # Ждем появления ответа
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"(//div[contains(@class, 'accordion__panel') and not(@hidden)])[{index + 1}]"))
        )
            answers = self.find_elements(self.locators.ANSWER_LOCATOR)
            if index < len(answers):
                return answers[index].text
        except:
            pass
        return None

    def click_order_button_top(self):
        self.click_element(self.locators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)

    def click_samokat_logo(self):
        self.click_element(self.locators.SAMOKAT_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)

    def get_current_url(self):
        return self.driver.current_url

    def is_home_page_displayed(self):
        return self.is_element_visible(self.locators.PAGE_TITLE)