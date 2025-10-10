import allure, javaproperties
from .base_page import BasePage
from .locators import SanPINPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class SanPINPage(BasePage):
    def new_file_exists(self):
        with allure.step('Проверка добавления стандарта'):
            count_button = self.page.locator(SanPINPageLocators.COUNT_100_BUTTON)
            count_button.click()
            assert self.is_element_present(SanPINPageLocators.TEST_NAME)