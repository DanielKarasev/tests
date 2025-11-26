import allure, javaproperties
from .base_list_page import BaseListPage
from .locators import BaseListPageLocators
from .locators import CoursesListPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class CoursesListPage(BaseListPage):
    def courses_list_correct(self):
        self.id_column_exist()
        self.name_column_exist()
        self.ed_level_column_exist()
        self.date_column_exist()

    def ed_level_column_exist(self):
        with allure.step('Проверка наличия столбца уровня образования'):
            self.is_element_present(CoursesListPageLocators.ADD_EDUCATION_LEVEL_COLUMN)

    def add_noo_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_test_name'])
            self.add_ed_level_noo()
            self.confirm_add()

    def add_ooo_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_test_name'])
            self.add_ed_level_ooo()
            self.confirm_add()

    def add_soo_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_test_name'])
            self.add_ed_level_soo()
            self.confirm_add()

    def add_wrong_name_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_ed_level_noo()
            self.confirm_add()

    def add_course_without_ed_level(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_test_name'])
            self.confirm_add()

    def add_wrong_ed_level_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_test_name'])
            self.add_ed_wrong_level()
            self.confirm_add()

    def add_ed_level_noo(self):
        with allure.step('Выбор уровня НОО'):
            add_ed_level_field = self.page.locator(CoursesListPageLocators.ADD_ED_LEVEL_FIELD)
            add_ed_level_field.type("НОО\n")

    def add_ed_level_ooo(self):
        with allure.step('Выбор уровня ООО'):
            add_ed_level_field = self.page.locator(CoursesListPageLocators.ADD_ED_LEVEL_FIELD)
            add_ed_level_field.type("ООО\n")

    def add_ed_level_soo(self):
        with allure.step('Выбор уровня СОО'):
            add_ed_level_field = self.page.locator(CoursesListPageLocators.ADD_ED_LEVEL_FIELD)
            add_ed_level_field.type("СОО\n")

    def add_ed_wrong_level(self):
        with allure.step('Ввод несуществующего уровня'):
            add_ed_level_field = self.page.locator(CoursesListPageLocators.ADD_ED_LEVEL_FIELD)
            add_ed_level_field.type("XYZ\n")

    def new_course_exist(self):
        with allure.step('Проверка появления предмета'):
            self.is_element_present(CoursesListPageLocators.NEW_COURSE)

    def new_course_not_exist(self):
        with allure.step('Проверка отсутствия предмета'):
            self.is_not_element_present(CoursesListPageLocators.NEW_COURSE)

    def edit_course_name(self):
        with allure.step('Редактирвоание названия курса'):
            self.open_edit_form()
            self.add_name(props['courses_new_test_name'])
            self.confirm_add()

    def changed_course_exist(self):
        with allure.step('Проверка появления изменённого имени предмета'):
            self.is_element_present(CoursesListPageLocators.CHANGED_COURSE)

    def add_changed_noo_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_new_test_name'])
            self.add_ed_level_noo()
            self.confirm_add()

    def add_changed_ooo_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_new_test_name'])
            self.add_ed_level_ooo()
            self.confirm_add()

    def add_changed_soo_course(self):
        with allure.step('Добавление предмета'):
            self.open_add_form()
            self.add_name(props['courses_new_test_name'])
            self.add_ed_level_soo()
            self.confirm_add()