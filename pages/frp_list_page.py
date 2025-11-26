import allure, datetime, javaproperties
from .base_list_page import BaseListPage
from .locators import BaseListPageLocators
from. locators import FRPListPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FRPListPage(BaseListPage):
    def frp_list_correct(self):
        self.base_list_correct()
        self.subject_column_exist()
        self.base_level_column_exist()

    def subject_column_exist(self):
        with allure.step('Проверка наличия колонки Предмета'):
            self.is_element_present(FRPListPageLocators.SUBJECT_COLUMN)

    def base_level_column_exist(self):
        with allure.step('Проверка наличия колонки Базового Уровня'):
            self.is_element_present(FRPListPageLocators.BASE_LEVEL_COLUMN)

    def add_full_archive_base_file(self):
        with allure.step('Добавление полного базового архивного файла'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_base_name(props['frp_test_base_name'])
            self.add_base_date()
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_base_status()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_archive_base_file_without_name(self):
        with allure.step('Добавление базового архивного файла без имени'):
            self.open_add_form()
            self.add_base_name(props['frp_test_base_name'])
            self.add_base_date()
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_base_status()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_archive_base_file_without_base_name(self):
        with allure.step('Добавление базового архивного файла без названия документа-основания'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_base_date()
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_base_status()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_archive_base_file_without_base_date(self):
        with allure.step('Добавление базового архивного файла без даты документа-основания'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_base_name(props['frp_test_base_name'])
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_base_status()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_archive_base_file_without_base_name_and_date(self):
        with allure.step('Добавление базового архивного файла без названия и даты документа-основания'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_base_status()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_archive_base_file_without_course(self):
        with allure.step('Добавление полного базового архивного файла'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_base_name(props['frp_test_base_name'])
            self.add_base_date()
            self.add_base_status()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_archive_base_file_without_pdf(self):
        with allure.step('Добавление базового архивного файла без пдф вложения'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_base_name(props['frp_test_base_name'])
            self.add_base_date()
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_base_status()
            self.add_archive_status()
            self.confirm_add()

    def add_archive_full_file(self):
        with allure.step('Добавление полного архивного файла'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_base_name(props['frp_test_base_name'])
            self.add_base_date()
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_archive_status()
            self.add_pdf()
            self.confirm_add()

    def add_full_base_file(self):
        with allure.step('Добавление полного базового файла'):
            self.open_add_form()
            self.add_name(props['frp_test_name'])
            self.add_base_name(props['frp_test_base_name'])
            self.add_base_date()
            self.add_ed_level_noo()
            self.add_course_name()
            self.add_base_status()
            self.add_pdf()
            self.confirm_add()

    def add_ed_level_noo(self):
        with allure.step('Заполнение поля Уровня Образования'):
            add_ed_level_field = self.page.locator(FRPListPageLocators.ADD_ED_LEVEL_FIELD)
            add_ed_level_field.type("НОО\n")

    def add_ed_level_ooo(self):
        with allure.step('Заполнение поля Уровня Образования'):
            add_ed_level_field = self.page.locator(FRPListPageLocators.ADD_ED_LEVEL_FIELD)
            add_ed_level_field.type("ООО\n")

    def add_ed_level_soo(self):
        with allure.step('Заполнение поля Уровня Образования'):
            add_ed_level_field = self.page.locator(FRPListPageLocators.ADD_ED_LEVEL_FIELD)
            add_ed_level_field.type("СОО\n")

    def add_course_name(self):
        with allure.step('Заполнение поля Предмета'):
            add_cource_field = self.page.locator(FRPListPageLocators.ADD_COURSE_FIELD)
            add_cource_field.type(f"{props['courses_test_name']}\n")

    def add_changed_course_name(self):
        with allure.step('Заполнение поля Предмета'):
            add_cource_field = self.page.locator(FRPListPageLocators.ADD_COURSE_FIELD)
            add_cource_field.type(f"{props['courses_new_test_name']}\n")

    def add_base_status(self):
        with allure.step('Указание статуса базового уровня'):
            base_level_checkbox = self.page.locator(FRPListPageLocators.BASE_LEVEL_CHECKBOX)
            base_level_checkbox.check()

    def file_exist(self):
        with allure.step('Проверка появления записи'):
            self.is_element_present(FRPListPageLocators.FILE_NAME)

    def file_not_exist(self):
        with allure.step('Проверка отсутствия записи'):
            self.is_not_element_present(FRPListPageLocators.FILE_NAME)

    def base_name_exist(self):
        with allure.step('Проверка наличия названия документа-основания'):
            assert self.is_element_present(FRPListPageLocators.BASE_NAME)

    def base_name_didnt_exist(self):
        with allure.step('Проверка отсутствия названия документа-основания'):
            self.is_not_element_present(FRPListPageLocators.BASE_NAME)

    def base_date_exist(self):
        with allure.step('Проверка наличия даты документа-основания'):
            assert self.is_element_present(BaseListPageLocators.BASE_DATE)

    def base_date_didnt_exist(self):
        with allure.step('Проверка отсутсвия даты документа-основания'):
            self.is_not_element_present(BaseListPageLocators.BASE_DATE)

    def base_status_false(self):
        with allure.step('Проверка того что запись не базового уровня'):
            base_status = self.page.locator(FRPListPageLocators.BASE_CHECK)
            assert base_status.inner_text() == "Нет"

    def base_status_true(self):
        with allure.step('Проверка того что запись базового уровня'):
            base_status = self.page.locator(FRPListPageLocators.BASE_CHECK)
            assert base_status.inner_text() == "Да"

    def edit_file_name(self):
        self.open_edit_form()
        self.add_name(props['frp_new_test_name'])
        self.confirm_add()

    def edit_base_name(self):
        self.open_edit_form()
        self.add_base_name(props['frp_new_test_base_name'])
        self.confirm_add()

    def edit_add_base_name(self):
        self.open_edit_form()
        self.add_base_name(props['frp_test_base_name'])
        self.confirm_add()

    def change_course(self):
        self.open_edit_form()
        self.add_ed_level_ooo()
        self.add_changed_course_name()
        self.confirm_add()

    def changed_course_name_exist(self):
        with allure.step('Проверка изменения названия предмета'):
            assert self.is_element_present(FRPListPageLocators.CHANGED_COURSE_NAME)

    def changed_name_exist(self):
        with allure.step('Проверка изменения имени записи'):
            assert self.is_element_present(FRPListPageLocators.NEW_FILE_NAME)

    def changed_base_name_exist(self):
        with allure.step('Проверка изменения названия документа-основания'):
            assert self.is_element_present(FRPListPageLocators.NEW_BASE_NAME)

    def open_frp_file(self):
        with allure.step('Открытие записи'):
            self.open_file(FRPListPageLocators.FILE_NAME)