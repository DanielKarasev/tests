import allure, javaproperties
from .base_page import BasePage
from .locators import FOOPPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FOOPPage(BasePage):

    def open_adapted_foops(self):
        with allure.step('Переключение страницы на адаптированные записи'):
            adapted_foops = self.page.locator(FOOPPageLocators.ADAPTED_FOOPS)
            adapted_foops.click()

    def show_at_100(self):
        button = self.page.locator(FOOPPageLocators.COUNT_100_BUTTON)
        button.click()

    def testfile_exists(self):
        with allure.step('Проверка появления тестовой записи'):
            assert self.is_element_present(FOOPPageLocators.TEST_NAME)

    def adapted_testfile_exists(self):
        self.open_adapted_foops()
        self.show_at_100()
        self.testfile_exists()