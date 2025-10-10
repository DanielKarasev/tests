import allure, datetime, javaproperties
from .base_site_page import BaseSitePage
from .locators import BaseSitePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class SanPINSitePage(BaseSitePage):
    def sanpin_page_correct(self):
        with allure.step('Проверка корректности компонентов страницы'):
            self.page_base_correct()
            self.name_correct()
            self.base_name_correct()

    def name_correct(self):
        with allure.step('Проверка корректности имени записи'):
            assert self.has_text(BaseSitePageLocators.TEST_NAME, props['sanpin_test_name'])

    def base_name_correct(self):
        with allure.step('Проверка корректности названия документа-основания'):
            assert self.has_text(BaseSitePageLocators.TEST_BASE_NAME, props['sanpin_test_base_name'])