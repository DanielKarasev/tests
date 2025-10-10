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
            self.fill_field(BaseListPageLocators.ADD_NAME_FIELD, name)

    def add_base_name(self, base_name):
        with allure.step('Добавление название документа-основания записи'):
            self.fill_field(BaseListPageLocators.ADD_BASE_NAME_FIELD, base_name)

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

    def delete_file_base_name(self):
        with allure.step('Удаление названия документа-основания'):
            self.open_edit_form()
            self.add_base_name('')
            self.confirm_add()

    def delete_file_base_date(self):
        with allure.step('Удаление даты документа-основания'):
            self.open_edit_form()
            self.delete_base_date()
            self.confirm_add()

    def base_date_didnt_exidt(self):
        with allure.step('Проверка отсутствия даты документа-основания'):
            self.is_not_element_present(BaseListPageLocators.BASE_DATE)

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

    def page_switch_to_next(self):
        with allure.step('Переключение на следующую страницу'):
            page_switch = self.page.locator(BaseListPageLocators.PAGE_FORWARD_BUTTON)
            page_switch.click()

    def page_switch_to_back(self):
        with allure.step('Переключение на предыдущую страницу'):
            page_switch = self.page.locator(BaseListPageLocators.PAGE_BACK_BUTTON)
            page_switch.click()

    def page_switch_to_one(self):
        with allure.step('Переключение на первую страницу'):
            page_switch = self.page.locator(BaseListPageLocators.PAGE_ONE)
            page_switch.click()

    def page_switch_to_two(self):
        with allure.step('Переключение на вторую страницу'):
            page_switch = self.page.locator(BaseListPageLocators.PAGE_TWO)
            page_switch.click()

    def checking_record_numbers(self):
        with allure.step('Проверка того какие записи на странице'):
            numbers = self.page.locator(BaseListPageLocators.RECORD_NUMBERS)
            return numbers.inner_text()

    def pagination_check_1(self):
        num_page_one = self.checking_record_numbers()
        self.page_switch_to_two()
        num_page_two = self.checking_record_numbers()
        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
            assert num_page_one != num_page_two

    def pagination_check_2(self):
        num_page_one = self.checking_record_numbers()
        self.page_switch_to_next()
        num_page_two = self.checking_record_numbers()
        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
            assert num_page_one != num_page_two

    def pagination_check_3(self):
        self.page_switch_to_next()
        num_page_one = self.checking_record_numbers()
        self.page_switch_to_one()
        num_page_two = self.checking_record_numbers()
        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
            assert num_page_one != num_page_two

    def pagination_check_4(self):
        self.page_switch_to_two()
        num_page_one = self.checking_record_numbers()
        self.page_switch_to_back()
        num_page_two = self.checking_record_numbers()
        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
            assert num_page_one != num_page_two