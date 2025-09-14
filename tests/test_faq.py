import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from data_test.data import Urls

@pytest.fixture
def driver():
    service = FirefoxService()
    drv = webdriver.Firefox(service=service)
    drv.get(Urls.BASE_URL)
    yield drv
    drv.quit()
import pytest
import allure
from pages.home_page import HomePage
from data_test.data import TestData

@allure.feature('Вопросы о важном')
class TestQuestions:
    @pytest.mark.parametrize('question_index,expected_answer', 
                             [(i, answer) for i, (_, answer) in enumerate(TestData.QUESTIONS_AND_ANSWERS)])
    @allure.title('Проверка ответа на вопрос №{question_index + 1}')
    def test_question_answer_correct(self, driver, question_index, expected_answer):
        """
        Тест проверяет, что при клике на вопрос отображается правильный ответ
        """
        with allure.step('Открыть главную страницу'):
            home_page = HomePage(driver)
            home_page.accept_cookies()
        
        with allure.step(f'Нажать на вопрос номер {question_index + 1}'):
            home_page.click_question(question_index)
        
        with allure.step('Проверить текст ответа'):
            actual_answer = home_page.get_answer_text(question_index)
            assert actual_answer == expected_answer, \
                f"Ожидаемый ответ: {expected_answer}, Фактический: {actual_answer}"
    
    @allure.title('Проверка сворачивания ответа при повторном клике')
    @pytest.mark.parametrize('question_index', [0, 1, 2])
    def test_answer_collapse_on_double_click(self, driver, question_index):
        """
        Тест проверяет, что ответ сворачивается при повторном клике на вопрос
        """
        with allure.step('Открыть главную страницу'):
            home_page = HomePage(driver)
            home_page.accept_cookies()
    
        with allure.step(f'Нажать на вопрос номер {question_index + 1} первый раз'):
            home_page.click_question(question_index)
    
        with allure.step('Проверить, что ответ отобразился'):
        # Добавляем ожидание
            import time
            time.sleep(1)
        
            answer_after_first_click = home_page.get_answer_text(question_index)
            assert answer_after_first_click is not None, "Ответ не отобразился после первого клика"
    
        with allure.step(f'Нажать на вопрос номер {question_index + 1} второй раз'):
            home_page.click_question(question_index)
    
        with allure.step('Проверить, что ответ скрылся'):
            time.sleep(1)
        
        # Проверяем, что ответ скрыт через атрибут
        questions = home_page.find_elements(home_page.locators.QUESTION_LOCATOR)
        if question_index < len(questions):
            # Получаем родительский элемент аккордеона
            accordion_item = questions[question_index].find_element(By.XPATH, "./ancestor::div[contains(@class, 'accordion__item')]")
            is_expanded = accordion_item.get_attribute("class")
            
            # Проверяем, что аккордеон свернут
            assert "accordion__item_active" not in is_expanded, "Ответ не скрылся после второго клика"