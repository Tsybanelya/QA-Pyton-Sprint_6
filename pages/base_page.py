from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Поиск элемента по локатору: {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Не найден элемент по локатору {locator}"
        )

    @allure.step("Поиск всех элементов по локатору: {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не найдены элементы по локатору {locator}"
        )

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator, timeout=10):
        el = self.find_element(locator, timeout)
        el.click()

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def input_text(self, locator, text, timeout=10):
        el = self.find_element(locator, timeout)
        el.clear()
        el.send_keys(text)

    @allure.step("Ожидание, когда элемент станет кликабельным: {locator}")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не стал кликабельным: {locator}"
        )

    @allure.step("Получение текста элемента: {locator}")
    def get_text(self, locator, timeout=10):
        el = self.find_element(locator, timeout)
        return el.text

    @allure.step("Проверка видимости элемента: {locator}")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание, когда элемент исчезнет: {locator}")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator),
            message=f"Элемент не исчез: {locator}"
        )

    @allure.step("Открытие базового URL")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Текущий дескриптор окна браузера")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получить новый дескриптор окна (после появления нового окна)")
    def get_new_window_handle(self, old_handle):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != old_handle:
                return handle
        raise Exception("Новое окно не появилось")

    @allure.step("Переключиться в окно браузера с дескриптором {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Ждать новое окно по сравнению с {old_handle}")
    def wait_for_new_window_opened(self, old_handle, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1 and any(h != old_handle for h in d.window_handles),
            message="Новое окно не появилось"
        )

    @allure.step("Ждать, что url содержит подстроку: {substring}")
    def wait_for_url_contains(self, substring, timeout=10):

        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(substring),
            message=f"URL не содержит '{substring}'"
        )
    @allure.step("Ждём, что элемент видим: {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым: {locator}"
        )