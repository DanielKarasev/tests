import pytest, allure, javaproperties
from pages.courses_list_page import CoursesListPage
from pages.login_page import LoginPage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['courses_list_link']

@pytest.fixture(scope="function", autouse=True)
def setup(page):
    with allure.step('Логирование'):
        courses_list_page = CoursesListPage(page, link)
        courses_list_page.open()
        login_page = LoginPage(page, courses_list_page.url)
        login_page.login()

@allure.story("Общие тесты")
@allure.title("Проверка целостности таблицы")
def test_list_correct(page):
    with allure.step('Открытие страницы'):
        coursers_list_page = CoursesListPage(page, link)
        coursers_list_page.open()
    coursers_list_page.courses_list_correct()

@allure.story("Общие тесты")
@allure.title("Удаление файла")
def test_delete_file(page):
    with allure.step('Открытие страницы'):
        coursers_list_page = CoursesListPage(page, link)
        coursers_list_page.open()
    coursers_list_page.add_noo_course()
    coursers_list_page.new_course_exist()
    coursers_list_page.delete_file()
    coursers_list_page.new_course_not_exist()

@allure.story("Создание неправильной записи")
@allure.title("Создание предмета без названия")
def test_add_wrong_name_course(page):
    with allure.step('Открытие страницы'):
        coursers_list_page = CoursesListPage(page, link)
        coursers_list_page.open()
    coursers_list_page.add_wrong_name_course()
    coursers_list_page.name_alert_correct()

@allure.story("Создание неправильной записи")
@allure.title("Создание предмета без названия уровня образования")
def test_add_course_without_ed_level(page):
    with allure.step('Открытие страницы'):
        coursers_list_page = CoursesListPage(page, link)
        coursers_list_page.open()
    coursers_list_page.add_course_without_ed_level()
    coursers_list_page.name_alert_correct()

@allure.story("Создание неправильной записи")
@allure.title("Создание предмета с вводом неправильного уровня образования")
def test_add_wrong_ed_level_course(page):
    with allure.step('Открытие страницы'):
        coursers_list_page = CoursesListPage(page, link)
        coursers_list_page.open()
    coursers_list_page.add_wrong_ed_level_course()
    coursers_list_page.name_alert_correct()

class TestsWithTrace():
    @pytest.fixture(scope="function", autouse=True)
    def teardown(self, page):
        yield
        coursers_list_page = CoursesListPage(page, link)
        coursers_list_page.open()
        coursers_list_page.delete_file()

    @allure.story("Создание записи")
    @allure.title("Создание предмета уровня НОО")
    def test_add_noo_course(self, page):
        with allure.step('Открытие страницы'):
            coursers_list_page = CoursesListPage(page, link)
            coursers_list_page.open()
        coursers_list_page.add_noo_course()
        coursers_list_page.new_course_exist()

    @allure.story("Создание записи")
    @allure.title("Создание предмета уровня ООО")
    def test_add_ooo_course(self, page):
        with allure.step('Открытие страницы'):
            coursers_list_page = CoursesListPage(page, link)
            coursers_list_page.open()
        coursers_list_page.add_ooo_course()
        coursers_list_page.new_course_exist()

    @allure.story("Создание записи")
    @allure.title("Создание предмета уровня СОО")
    def test_add_soo_course(self, page):
        with allure.step('Открытие страницы'):
            coursers_list_page = CoursesListPage(page, link)
            coursers_list_page.open()
        coursers_list_page.add_soo_course()
        coursers_list_page.new_course_exist()

    @allure.story("Изменение записи")
    @allure.title("Изменение имени")
    def test_edit_file_name(self, page):
        with allure.step('Открытие страницы'):
            coursers_list_page = CoursesListPage(page, link)
            coursers_list_page.open()
        coursers_list_page.add_noo_course()
        coursers_list_page.new_course_exist()
        coursers_list_page.edit_course_name()
        coursers_list_page.changed_course_exist()