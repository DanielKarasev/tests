import allure, datetime
from .base_page import BasePage
from .locators import BaseListPageLocators

class BaseListPage(BasePage):
    def base_list_correct(self):
        with allure.step('Проверка целостности базовых пунктов таблицы'):
            self.id_column_exist()
            self.name_column_exist()
            self.base_name_column_exist()
            self.base_date_column_exist()
            self.pdf_link_column_exist()
            self.archive_column_exist()
            self.date_column_exist()

    def id_column_exist(self):
        with allure.step('Проверка наличия колонки ID'):
            assert self.is_element_present(BaseListPageLocators.ID_COLUMN)

    def name_column_exist(self):
        with allure.step('Проверка наличия колонки Названия'):
            assert self.is_element_present(BaseListPageLocators.NAME_COLUMN)

    def base_name_column_exist(self):
        with allure.step('Проверка наличия колонки Названия документа-основания'):
            assert self.is_element_present(BaseListPageLocators.BASE_NAME_COLUMN)

    def base_date_column_exist(self):
        with allure.step('Проверка наличия колонки даты документа-основания'):
            assert self.is_element_present(BaseListPageLocators.BASE_DATE_COLUMN)

    def pdf_link_column_exist(self):
        with allure.step('Проверка наличия колонки файла'):
            assert self.is_element_present(BaseListPageLocators.LINK_COLUMN)

    def archive_column_exist(self):
        with allure.step('Проверка наличия колонки архивного статуса'):
            assert self.is_element_present(BaseListPageLocators.ARCHIVE_COLUMN)

    def date_column_exist(self):
        with allure.step('Проверка наличия колонки даты создания записи'):
            assert self.is_element_present(BaseListPageLocators.DATE_COLUMN)

    def open_add_form(self):
        with allure.step('Открытие формы создания записи'):
            add_button = self.page.locator(BaseListPageLocators.ADD_BUTTON)
            add_button.click()

    def add_name(self, name):
        with allure.step('Добавление названия записи'):
            add_name_field = self.page.locator(BaseListPageLocators.ADD_NAME_FIELD)
            add_name_field.fill(name)

    def add_base_name(self, base_name):
        with allure.step('Добавление название документа-основания записи'):
            add_base_name_field = self.page.locator(BaseListPageLocators.ADD_BASE_NAME_FIELD)
            add_base_name_field.fill(base_name)

    def add_base_date(self):
        with allure.step('Добавление даты документа-основания записи'):
            add_base_date_field = self.page.locator(BaseListPageLocators.ADD_BASE_DATE_FIELD)
            add_base_date_field.type(f'{(datetime.datetime.today() - datetime.timedelta(1)).strftime("%d.%m.%Y")}\n')

    def add_archive_status(self):
        with allure.step('Пометка файла как архивного'):
            archive_checkbox = self.page.locator(BaseListPageLocators.ARCHIVE_CHECKBOX)
            archive_checkbox.check()

    def add_pdf(self):
        with allure.step('Добавление pdf файла'):
            add_pdf_button = self.page.locator(BaseListPageLocators.ADD_PDF_BUTTON)
            add_pdf_button.set_input_files("Тест-основание.pdf")

    def confirm_add(self):
        with allure.step('Подтверждение создания записи'):
            confirm_add_button = self.page.locator(BaseListPageLocators.ADD_CONFIRM_BUTTON)
            confirm_add_button.click()

    def open_edit_form(self):
        with allure.step('Открытие формы редактирования записи'):
            edit_button = self.page.locator(BaseListPageLocators.EDIT_BUTTON)
            edit_button.click()

    def delete_base_date(self):
        with allure.step('Удаление даты документа-основания'):
            delete_button = self.page.locator(BaseListPageLocators.CLEAR_DATE_BUTTON)
            delete_button.click()

    def delete_file(self):
        with allure.step('Удаление записи'):
            delete_file_button = self.page.locator(BaseListPageLocators.DELETE_BUTTON)
            delete_file_button.click()
            delete_confirm_buttton = self.page.locator(BaseListPageLocators.DELETE_CONFIRM_BUTTON)
            delete_confirm_buttton.click()

    def name_alert_correct(self):
        with allure.step('Проверка появления предупреждения о необходимости имени'):
            assert self.is_element_present(BaseListPageLocators.ADD_NAME_ALERT)

    def date_alert_correct(self):
        with allure.step('Проверка появления предупреждения о необходимости даты'):
            assert self.is_element_present(BaseListPageLocators.ADD_BASE_DATE_ALERT)

    def pdf_alert_correct(self):
        with allure.step('Проверка появления предупреждения о необходимости PDF файла'):
            assert self.is_element_present(BaseListPageLocators.ADD_PDF_ALERT)