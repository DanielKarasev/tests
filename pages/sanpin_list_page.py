import allure, javaproperties
from .base_list_page import BaseListPage
from .locators import BaseListPageLocators
from .locators import SanPINListPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class SanPINListPage(BaseListPage):
    def add_full_file(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_base_name(props['sanpin_test_base_name'])
            self.add_base_date()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def file_exist(self):
        with allure.step('Проверека появления записи'):
            assert self.is_element_present(SanPINListPageLocators.TEST_NAME)

    def new_file_name_exist(self):
        with allure.step('Проверка того что название записи изменилось'):
            assert self.is_element_present(SanPINListPageLocators.NEW_TEST_NAME)

    def file_dont_exist(self):
        with allure.step('Проверка отсутсвия записи'):
            self.is_not_element_present(SanPINListPageLocators.TEST_NAME)

    def edit_file_name(self):
        with allure.step('Изменение имени записи'):
            self.open_edit_form()
            self.add_name(props['sanpin_new_test_name'])
            self.confirm_add()

    def base_name_didnt_exidt(self):
        with allure.step('Проверка отсутствия имени документа-основания'):
            self.is_not_element_present(SanPINListPageLocators.BASE_NAME)

    def add_file_without_name(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_base_name(props['sanpin_test_base_name'])
            self.add_base_date()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_base_name(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_base_date()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_base_date(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_base_name(props['sanpin_test_base_name'])
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_base_name_and_date(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_pdf(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_base_name(props['sanpin_test_base_name'])
            self.add_base_date()
            self.add_archive_status()
            self.confirm_add()

    def add_file_base_name(self):
        with allure.step('Добавление названия документа-основания'):
            self.open_edit_form()
            self.add_base_name(props['sanpin_test_base_name'])
            self.confirm_add()

    def add_file_base_date(self):
        with allure.step('Добавление даты документа-основания'):
            self.open_edit_form()
            self.add_base_date()
            self.confirm_add()

    def edit_file_base_name(self):
        with allure.step('Изменение названия документа-основания'):
            self.open_edit_form()
            self.add_base_name(props['sanpin_new_test_base_name'])
            self.confirm_add()

    def add_unarchived_file(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_base_name(props['sanpin_test_base_name'])
            self.add_base_date()
            self.add_pdf()
            self.confirm_add()

    def add_unarchived_file_without_base_name(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_base_date()
            self.add_pdf()
            self.confirm_add()

    def add_unarchived_file_without_base_date(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_base_name(props['sanpin_test_base_name'])
            self.add_pdf()
            self.confirm_add()

    def add_unarchived_file_without_base_name_and_date(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['sanpin_test_name'])
            self.add_pdf()
            self.confirm_add()

    def open_add_file(self):
        with allure.step('Открытие тестовой записи'):
            self.open_file(SanPINListPageLocators.TEST_NAME)

    def file_base_name_dont_exist(self):
        with allure.step('Проверка отсутсвия названия документа-оснсования'):
            self.is_not_element_present(SanPINListPageLocators.BASE_NAME)

    def file_base_date_dont_exist(self):
        with allure.step('Проверка отсутствия даты документа-основания'):
            self.is_not_element_present(BaseListPageLocators.BASE_DATE)

    def base_name_exist(self):
        with allure.step('Проверка наличия названия документа-основания'):
            assert self.is_element_present(SanPINListPageLocators.BASE_NAME)

    def base_date_exist(self):
        with allure.step('Проверка наличия  даты документа-основания'):
            assert self.is_element_present(BaseListPageLocators.BASE_DATE)