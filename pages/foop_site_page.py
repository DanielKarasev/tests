import allure, javaproperties
from .base_site_page import BaseSitePage
from .locators import BaseSitePageLocators
from .locators import FOOPSitePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FOOPSitePage(BaseSitePage):
    def foop_page_exist(self):
        self.page_base_exist()
        self.adapted_status_exist()

    def adapted_status_exist(self):
        with allure.step('Проверка наличия строки с указателем адаптированности'):
            assert self.is_element_present(FOOPSitePageLocators.ADAPTED_LINE)

    def foop_page_correct(self):
        with allure.step('Проверка корректности компонентов страницы'):
            self.page_base_correct()
            self.name_correct()
            self.base_name_correct()
            self.adapted_correct()

    def name_correct(self):
        with allure.step('Проверка корректности имени записи'):
            assert self.has_text(BaseSitePageLocators.TEST_NAME, props['foop_test_name'])

    def base_name_correct(self):
        with allure.step('Проверка корректности названия документа-основания'):
            assert self.has_text(BaseSitePageLocators.TEST_BASE_NAME, props['foop_test_base_name'])

    def adapted_correct(self):
        with allure.step('Проверка того что поле адапртированности соответвует введённому при создании записи'):
            assert self.has_text(FOOPSitePageLocators.ADAPTED_CONDITION, "Да")