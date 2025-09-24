import allure, datetime, javaproperties
from .base_page import BasePage
from .locators import BaseSitePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class BaseSitePage(BasePage):

    def page_base_exist(self):
        with allure.step('Проверка наличия базовых компонентнов'):
            self.id_line_exist()
            self.name_line_exist()
            self.base_name_line_exist()
            self.autor_line_exist()
            self.base_name_line_exist()
            self.link_line_exist()
            self.date_line_exist()
            self.archive_line_exist()

    def id_line_exist(self):
        with allure.step('Проверка наличия линии с ID'):
            self.is_element_present(BaseSitePageLocators.ID_LINE)

    def name_line_exist(self):
        with allure.step('Проверка наличия линии с названием запиис'):
            self.is_element_present(BaseSitePageLocators.NAME_LINE)

    def base_name_line_exist(self):
        with allure.step('Проверка наличия линии с названием документа-основания'):
            self.is_element_present(BaseSitePageLocators.BASE_NAME_LINE)

    def autor_line_exist(self):
        with allure.step('Проверка наличия линии с именем автора'):
            self.is_element_present(BaseSitePageLocators.AUTOR_LINE)

    def link_line_exist(self):
        with allure.step('Проверка наличия линии с ссылкой на PDF файл'):
            self.is_element_present(BaseSitePageLocators.LINK_LINE)

    def date_line_exist(self):
        with allure.step('Проверка наличия линии с датой создания записи'):
            self.is_element_present(BaseSitePageLocators.DATE_LINE)

    def archive_line_exist(self):
        with allure.step('Проверка наличия линии со статусом архивности'):
            self.is_element_present(BaseSitePageLocators.ARCHIVE_LINE)

    def page_base_correct(self):
        with allure.step('Проверка корректности базовых компонентов'):
            self.autor_correct()
            self.base_date_correct()
            self.date_correct()
            self.pdf_correct()
            self.archive_correct()

    def autor_correct(self):
        with allure.step('Проерка соответствия имени автора записи'):
            assert self.has_text(BaseSitePageLocators.AUTOR, props['username'])

    def base_date_correct(self):
        with allure.step('Проерка соответствия даты документа-основания'):
            assert self.has_text(BaseSitePageLocators.BASE_DATE, (datetime.datetime.today() - datetime.timedelta(1)).strftime("%d.%m.%Y"))

    def date_correct(self):
        with allure.step('Проерка соответствия имени даты создания записи'):
            assert self.has_text(BaseSitePageLocators.DATE, datetime.datetime.today().strftime("%d.%m.%Y"))

    def pdf_correct(self):
        with allure.step('Проерка соответствия имени pdf файла'):
            element = self.page.locator(BaseSitePageLocators.FILE_NAME)
            assert 'Тест-основание' in element.inner_text()

    def archive_correct(self):
        with allure.step('Проерка соответствия архивного статуса'):
            assert self.has_text(BaseSitePageLocators.ARCHIVE_CONDITION, 'Да')