import allure, javaproperties
from .base_site_page import BaseSitePage
from .locators import BaseSitePageLocators
from .locators import FRPSitePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FRPSitePage(BaseSitePage):
    def frp_page_exist(self):
        self.page_base_exist()
        self.base_status_exist()
        self.course_exist()

    def base_status_exist(self):
        with allure.step('Проверка наличия строки с укзанием того является ли уровень программы базовым'):
            assert self.is_element_present(FRPSitePageLocators.BASE_LEVEL_LINE)

    def course_exist(self):
        with allure.step('роверка наличия строки с названием курса'):
            assert self.is_element_present(FRPSitePageLocators.COURSE_LINE)

    def frp_page_correct(self):
        self.page_base_correct()
        self.name_correct()
        self.base_name_correct()
        self.base_status_correct()
        self.course_correct()

    def name_correct(self):
        with allure.step('Проверка корректности имени записи'):
            assert self.has_text(BaseSitePageLocators.TEST_NAME, props['frp_test_name'])

    def base_name_correct(self):
        with allure.step('Проверка корректности названия документа-основания'):
            assert self.has_text(BaseSitePageLocators.TEST_BASE_NAME, props['frp_test_base_name'])

    def base_status_correct(self):
        with allure.step('Проверка того что поле базового уровня соответвует введённому при создании записи'):
            assert self.has_text(FRPSitePageLocators.BASE_LEVEL_CONDITION, "Да")

    def course_correct(self):
        with allure.step('Проверка корректности названия тестового курса'):
            assert self.has_text(FRPSitePageLocators.COURSE, props['courses_test_name'])