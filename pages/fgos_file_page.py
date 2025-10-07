import allure, javaproperties
from .base_page import BasePage
from .locators import FGOSFilePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FGOSFilePage(BasePage):
    def tested_file_exist(self):
        with allure.step('тестовый файл существует'):
            assert self.is_element_present(FGOSFilePageLocators.TEST_FILE_NAME)