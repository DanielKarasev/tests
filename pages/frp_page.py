import allure, javaproperties, time
from .base_page import BasePage
from .locators import FRPPageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class FRPPage(BasePage):

    def show_at_100(self):
        button = self.page.locator(FRPPageLocators.COUNT_100_BUTTON)
        button.click()

    def testfile_check(self):
        with allure.step('Проверка появления тестовой записи'):
            assert self.is_element_present(FRPPageLocators.TEST_NAME)

    def testfile_exists(self):
        self.show_at_100()
        self.testfile_check()

    def current_quantity(self):
        with allure.step('Проверка количества документов в разделе'):
            quantity = self.page.wait_for_selector(FRPPageLocators.NUMBER_OF_DOCUMENTS)
            return quantity.inner_text()

    def clear_choice_field(self):
        with allure.step('Очистка окна фильтрации'):
            self.open_file(FRPPageLocators.CLEAR_CHOICE_FIELD)

    def choice_ed_level_noo(self):
        with allure.step('Фильтрация документов по уровню образования НОО'):
            with allure.step('Открытие списка фильтрации'):
                self.open_file(FRPPageLocators.ED_LEVEL_CHOICE_FIELD)
            with allure.step('Выбор НОО'):
                self.open_file(FRPPageLocators.ED_LEVEL_NOO)

    def choice_ed_level_ooo(self):
        with allure.step('Фильтрация документов по уровню образования ООО'):
            with allure.step('Открытие списка фильтрации'):
                self.open_file(FRPPageLocators.ED_LEVEL_CHOICE_FIELD_NOO)
            with allure.step('Выбор ООО'):
                self.open_file(FRPPageLocators.ED_LEVEL_OOO)

    def choice_ed_level_soo(self):
        with allure.step('Фильтрация документов по уровню образования СОО'):
            with allure.step('Открытие списка фильтрации'):
                self.open_file(FRPPageLocators.ED_LEVEL_CHOICE_FIELD_OOO)
            with allure.step('Выбор СОО'):
                self.open_file(FRPPageLocators.ED_LEVEL_SOO)

    def open_choice_course_field(self):
        with allure.step('Открытие формы выбора учебного предмета, курса'):
            self.open_file(FRPPageLocators.COURSE_CHOICE_FIELD)

    def choice_course(self):
        with allure.step('Фильтрация документов по названию тестового курса'):
            self.open_choice_course_field()
            with allure.step('Выбор тестового курса'):
                self.open_file(FRPPageLocators.TEST_COURSE)

    def choice_base_level(self):
        with allure.step('Фильтрация документов по базовому уровню предметов'):
            with allure.step('Открытие списка фильтрации'):
                self.open_file(FRPPageLocators.COURSE_LEVEL_CHOICE_FIELD)
            with allure.step('Выбор базового уровня'):
                self.open_file(FRPPageLocators.COURSE_LEVEL_BASE)

    def choice_deep_level(self):
        with allure.step('Фильтрация документов по углублённому уровню предметов'):
            with allure.step('Открытие списка фильтрации'):
                self.open_file(FRPPageLocators.COURSE_LEVEL_CHOICE_FIELD_BASE_LEVEL)
            with allure.step('Выбор углублённого уровня'):
                self.open_file(FRPPageLocators.COURSE_LEVEL_DEEP)

    def ed_level_field_testing(self):
        with allure.step('Проверка фильтрации записей по уровню образования'):
            general_number_of_documents = self.current_quantity()
            self.choice_ed_level_noo()
            time.sleep(1)
            noo_number_of_documents = self.current_quantity()
            self.choice_ed_level_ooo()
            time.sleep(1)
            ooo_number_of_documents = self.current_quantity()
            self.choice_ed_level_soo()
            time.sleep(1)
            soo_number_of_documents = self.current_quantity()
            self.clear_choice_field()
            time.sleep(1)
            with allure.step('Сравнение количества документов при фильтрациях и без'):
                assert (general_number_of_documents != noo_number_of_documents) and (general_number_of_documents != soo_number_of_documents) and (general_number_of_documents != ooo_number_of_documents)

    def course_field_testing(self):
        with allure.step('Проверка фильтрации записей по курсу'):
            general_number_of_documents = self.current_quantity()
            self.choice_course()
            time.sleep(1)
            course_number_of_documents = self.current_quantity()
            self.clear_choice_field()
            time.sleep(1)
            with allure.step('Сравнение количества документов при фильтраци и без'):
                assert (general_number_of_documents != course_number_of_documents)

    def course_level_field_testing(self):
        with allure.step('Проверка фильтрации записей по уровню предмета'):
            general_number_of_documents = self.current_quantity()
            self.choice_base_level()
            time.sleep(1)
            base_number_of_documents = self.current_quantity()
            self.choice_deep_level()
            time.sleep(1)
            deep_number_of_documents = self.current_quantity()
            self.clear_choice_field()
            with allure.step('Сравнение количества документов при фильтрациях и без'):
                assert (general_number_of_documents != base_number_of_documents) and (general_number_of_documents != deep_number_of_documents)