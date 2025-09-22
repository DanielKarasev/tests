import allure, datetime, javaproperties
from .base_list_page import BaseListPage
from .locators import FGOSListPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FGOSListPage(BaseListPage):
    def add_full_file(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['fgos_test_name'])
            self.add_base_name(props['fgos_test_base_name'])
            self.add_base_date()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def file_exist(self):
        with allure.step('Проверека появления записи'):
            assert self.is_element_present(FGOSListPageLocators.TEST_NAME)

    def new_file_name_exist(self):
        with allure.step('Проверка того что название записи изменилось'):
            assert self.is_element_present(FGOSListPageLocators.NEW_TEST_NAME)

    def new_file_base_name_exist(self):
        with allure.step('Проверка того что название записи изменилось'):
            assert self.is_element_present(FGOSListPageLocators.NEW_TEST_BASE_NAME)

    def file_dont_exist(self):
        with allure.step('Проверка отсутсвия записи'):
            self.is_not_element_present(FGOSListPageLocators.TEST_NAME)

    def edit_file_name(self):
        with allure.step('<UNK> <UNK> <UNK>'):
            self.open_edit_form()
            self.add_name(props['new_fgos_test_name'])
            self.confirm_add()

    def add_file_without_name(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_base_name(props['fgos_test_base_name'])
            self.add_base_date()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_base_name(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['fgos_test_name'])
            self.add_base_date()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_base_date(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['fgos_test_name'])
            self.add_base_name(props['fgos_test_base_name'])
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_file_without_pdf(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['fgos_test_name'])
            self.add_base_name(props['fgos_test_base_name'])
            self.add_base_date()
            self.add_archive_status()
            self.confirm_add()

    def edit_file_base_name(self):
        with allure.step('Изменение названия документа-основания'):
            self.open_edit_form()
            self.add_base_name(props['new_fgos_test_base_name'])
            self.confirm_add()

    def add_unarchived_file(self):
        with allure.step('Добавление записи'):
            self.open_add_form()
            self.add_name(props['fgos_test_name'])
            self.add_base_name(props['fgos_test_base_name'])
            self.add_base_date()
            self.add_pdf()
            self.confirm_add()