import pytest
import allure
from pages.home_page import HomePage
from data_test.data import TestData

@allure.feature('Вопросы о важном')
class TestQuestions:
    @pytest.mark.parametrize(
        'question_index,expected_answer',
        [(i, answer) for i, (_, answer) in enumerate(TestData.QUESTIONS_AND_ANSWERS)]
    )
    @allure.title('Проверка ответа на вопрос №{question_index + 1}')
    def test_question_answer_correct(self, driver, question_index, expected_answer):
        """Проверяет, что при клике на вопрос отображается правильный ответ."""
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()
        home_page.click_question(question_index)
        # Ждём появления и сравниваем ответ по индексу
        actual_answer = home_page.get_answer_text()
        assert actual_answer == expected_answer, (
            f"Ожидаемый ответ: {expected_answer}, Фактический: {actual_answer}"
        )

    @allure.title('Проверка сворачивания ответа при повторном клике')
    @pytest.mark.parametrize('question_index', [0, 1, 2])
    def test_answer_collapse_on_double_click(self, driver, question_index):
        """Проверяет, что ответ сворачивается при повторном клике на вопрос."""
        home_page = HomePage(driver)
        home_page.open()
        home_page.accept_cookies()

        # Первый клик — открытие ответа (ждём появления!)
        home_page.click_question(question_index)
        assert home_page.is_answer_visible(), "Ответ не отобразился после первого клика"

        # Второй клик — закрытие ответа (ждём исчезновения!)
        home_page.click_question(question_index)
        home_page.wait_for_answer_disappear()

        # Проверяем, что вопрос теперь свернут (всё внутри PageObject)
        assert home_page.is_question_collapsed(question_index), "Ответ не скрылся после второго клика"