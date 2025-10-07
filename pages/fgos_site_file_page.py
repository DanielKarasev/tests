import allure, datetime, javaproperties
from .base_page import BasePage
from .locators import FGOSSiteFilePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

base_date = (datetime.datetime.today() - datetime.timedelta(1)).strftime("%d.%m.%Y")
date = datetime.datetime.today().strftime("%d.%m.%Y")

class FGOSSiteFilePage(BasePage):
    def page_correct(self):
        self.correct_design()
        self.file_correct()

    def correct_design(self):
        with allure.step('Проверка корректности макета страницы'):
            self.id_line_exist()
            self.name_line_exist()
            self.autor_line_exist()
            self.file_name_line_exist()
            self.date_line_exist()
            self.base_date_line_exist()

    def id_line_exist(self):
        with allure.step('Проверка наличия поля ID'):
            assert self.is_element_present(FGOSSiteFilePageLocators.ID_LINE)

    def name_line_exist(self):
        with allure.step('Проверка наличия поля имени записи'):
            assert self.is_element_present(FGOSSiteFilePageLocators.NAME_LINE)

    def autor_line_exist(self):
        with allure.step('Проверка наличия поля имени автора'):
            assert self.is_element_present(FGOSSiteFilePageLocators.AUTOR_LINE)

    def file_name_line_exist(self):
        with allure.step('Проверка наличия поля прикреплённого pdf файла'):
            assert self.is_element_present(FGOSSiteFilePageLocators.FILE_LINE)

    def date_line_exist(self):
        with allure.step('Проверка наличия поля даты создания записи'):
            assert self.is_element_present(FGOSSiteFilePageLocators.DATE_LINE)

    def base_date_line_exist(self):
        with allure.step('Проверка наличия поля даты документа-оснвоания'):
            assert self.is_element_present(FGOSSiteFilePageLocators.BASE_DATE)

    def file_correct(self):
        with allure.step('Проверка корректности данных записи'):
            self.name_correct()
            self.autor_correct()
            self.file_name_correct()
            self.date_correct()
            self.base_date_correct()

    def name_correct(self):
        with allure.step('Проверка корректности названия записи'):
            assert self.has_text(FGOSSiteFilePageLocators.NAME, props['fgos_file_name'])

    def autor_correct(self):
        with allure.step('Проверка корректности имени автора'):
            assert self.has_text(FGOSSiteFilePageLocators.AUTOR, props['username'])

    def file_name_correct(self):
        with allure.step('Проверка корректности названия прикреплённого pdf файла'):
            file_name = self.page.locator(FGOSSiteFilePageLocators.FILE_NAME)
            assert 'Тест-основание' in file_name.inner_text()

    def date_correct(self):
        with allure.step('Проверка корректности даты создания записи'):
            assert self.has_text(FGOSSiteFilePageLocators.DATE, date)

    def base_date_correct(self):
        with allure.step('Проверка корректности даты документа-основания'):
            assert self.has_text(FGOSSiteFilePageLocators.BASE_DATE, base_date)