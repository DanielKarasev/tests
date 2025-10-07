import allure, javaproperties
from .base_page import BasePage
from .locators import FGOSPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FGOSPage(BasePage):
    def new_file_exists(self):
        with allure.step('Проверка добавления стандарта'):
            assert self.is_element_present(FGOSPageLocators.TEST_NAME)

    def open_new_file(self):
        with allure.step('Открытие тестового стандарта'):
            self.open_file(FGOSPageLocators.TEST_NAME)

