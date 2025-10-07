import allure, datetime, javaproperties
from .base_site_page import BaseSitePage
from .locators import FGOSSitePageLocators
from .locators import BaseSitePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FGOSSitePage(BaseSitePage):
    def fgos_page_correct(self):
        with allure.step('Проверка корректности компонентов страницы'):
            self.page_base_correct()
            self.name_correct()
            self.base_name_correct()

    def name_correct(self):
        with allure.step('Проверка корректности имени записи'):
            assert self.has_text(BaseSitePageLocators.TEST_NAME, props['fgos_test_name'])

    def base_name_correct(self):
        with allure.step('Проверка корректности названия документа-основания'):
            assert self.has_text(BaseSitePageLocators.TEST_BASE_NAME, props['foop_test_base_name'])

    def table_correct(self):
        with allure.step('Проверка целостности таблицы'):
            self.id_column_exist()
            self.name_column_exist()
            self.date_column_exist()
            self.base_date_column_exist()
            self.link_column_exist()

    def id_column_exist(self):
        with allure.step('Проверка наличия столбца с id записи'):
            assert self.is_element_present(FGOSSitePageLocators.ID_COLUMN)

    def name_column_exist(self):
        with allure.step('Проверка наличия столбца с названием файла'):
            assert self.is_element_present(FGOSSitePageLocators.NAME_COLUMN)

    def date_column_exist(self):
        with allure.step('Проверка наличия столбца с датой создания записи'):
            assert self.is_element_present(FGOSSitePageLocators.DATE_COLUMN)

    def base_date_column_exist(self):
        with allure.step('Проверка наличия столбца с датой документа-основания'):
            assert self.is_element_present(FGOSSitePageLocators.BASE_DATE_COLUMN)

    def link_column_exist(self):
        with allure.step('Проверка наличия столбца с ссылкой на pdf файл'):
            assert self.is_element_present(FGOSSitePageLocators.LINK_COLUMN)

    def add_file(self):
        with allure.step('Добавление записи к стандарту'):
            with allure.step('Открытие формы добавления записи'):
                self.open_file(FGOSSitePageLocators.ADD_FILE_BUTTON)
            with allure.step('Ввод названия файла'):
                self.fill_field(FGOSSitePageLocators.ADD_NAME_FIELD, props['fgos_file_name'])
            self.fill_base_date()
            self.add_pdf()
            self.confirm_add()

    def fill_base_date(self):
        with allure.step('Ввод даты документа-основания'):
            add_base_date_field = self.page.locator(FGOSSitePageLocators.ADD_BASE_DATE_FIELD)
            add_base_date_field.type(f'{(datetime.datetime.today() - datetime.timedelta(1)).strftime("%d.%m.%Y")}\n')

    def add_pdf(self):
        with allure.step('Добавление pdf файла'):
            add_pdf_button = self.page.locator(FGOSSitePageLocators.ADD_PDF_BUTTON)
            add_pdf_button.set_input_files("Тест-основание.pdf")

    def confirm_add(self):
        with allure.step('Подтверждение добавления файла'):
            add_confirm_button = self.page.locator(FGOSSitePageLocators.ADD_CONFIRM_BUTTON)
            add_confirm_button.click()

    def new_file_exist(self):
        with allure.step('Проверка появления нового файла'):
            assert self.is_element_present(FGOSSitePageLocators.NEW_FILE_NAME)

    def new_file_didnt_exist(self):
        with allure.step(f'Проверка того что запись с названием {props['fgos_file_name']} не отображается'):
            self.is_not_element_present(FGOSSitePageLocators.NEW_FILE_NAME)

    def add_file_without_name(self):
        with allure.step('Попытка добавление записи к стандарту'):
            with allure.step('Открытие формы добавления записи'):
                self.open_file(FGOSSitePageLocators.ADD_FILE_BUTTON)
            self.fill_base_date()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_base_date(self):
        with allure.step('Попытка добавление записи к стандарту'):
            with allure.step('Открытие формы добавления записи'):
                self.open_file(FGOSSitePageLocators.ADD_FILE_BUTTON)
            with allure.step('Ввод названия файла'):
                self.fill_field(FGOSSitePageLocators.ADD_NAME_FIELD, props['fgos_file_name'])
            self.add_pdf()
            self.confirm_add()

    def add_file_without_pdf(self):
        with allure.step('Попытка добавление записи к стандарту'):
            with allure.step('Открытие формы добавления записи'):
                self.open_file(FGOSSitePageLocators.ADD_FILE_BUTTON)
            with allure.step('Ввод названия файла'):
                self.fill_field(FGOSSitePageLocators.ADD_NAME_FIELD, props['fgos_file_name'])
            self.fill_base_date()
            self.confirm_add()

    def name_allert_correct(self):
        with allure.step('Проверка появления сообщения об ошибке'):
            assert self.is_element_present(FGOSSitePageLocators.ADD_NAME_ALERT)

    def base_date_allert_correct(self):
        with allure.step('Проверка появления сообщения об ошибке'):
            assert self.is_element_present(FGOSSitePageLocators.ADD_BASE_DATE_ALERT)

    def pdf_allert_correct(self):
        with allure.step('Проверка появления сообщения об ошибке'):
            assert self.is_element_present(FGOSSitePageLocators.ADD_PDF_ALERT)

    def delete_file(self):
        with allure.step("удаление файла"):
            self.open_file(FGOSSitePageLocators.DELETE_BUTTON)
            self.open_file(FGOSSitePageLocators.DELETE_CONFIRM_BUTTON)

    def edit_file(self):
        with allure.step('Открытие формы редактирвания'):
            self.open_file(FGOSSitePageLocators.EDIT_BUTTON)
        with allure.step('Изменение имени файла'):
            self.fill_field(FGOSSitePageLocators.ADD_NAME_FIELD, props['new_fgos_file_name'])
        with allure.step('Подтверждение изменений'):
            self.open_file(FGOSSitePageLocators.ADD_CONFIRM_BUTTON)

    def new_file_name_exist(self):
        with allure.step(f'Проверка того что запись с названием {props['new_fgos_file_name']} отображается'):
            assert self.is_element_present(FGOSSitePageLocators.EDIT_FILE_NAME)

    def new_file_name_didnt_exist(self):
        with allure.step(f'Проверка того что запись с названием {props['new_fgos_file_name']} не отображается'):
            self.is_not_element_present(FGOSSitePageLocators.EDIT_FILE_NAME)

    def find_file(self, what):
        with allure.step('Открытие фильра по именам'):
            self.open_file(FGOSSitePageLocators.NAME_FILTER_BUTTON)
        with allure.step('Ввод имени искомой записи'):
            self.fill_field(FGOSSitePageLocators.NAME_FILTER_FIELD, what)
        with allure.step('Фильтрация списка записей'):
            self.open_file(FGOSSitePageLocators.NAME_FILTER_CONFIRM_BUTTON)

    def add_file_open(self):
        with allure.step('Открытие созданной записи'):
            self.open_file(FGOSSitePageLocators.NEW_FILE_NAME)