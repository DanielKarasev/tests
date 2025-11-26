import pytest, allure, javaproperties

from pages import frp_list_page
from pages.courses_list_page import CoursesListPage
from pages.frp_page import FRPPage
from pages.login_page import LoginPage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['frp_link']
courses_list_link = props['courses_list_link']

@pytest.fixture(scope="function", autouse=True)
def setup(page):
    with allure.step('Логирование'):
        courses_list_page = CoursesListPage(page, courses_list_link)
        courses_list_page.open()
        login_page = LoginPage(page, courses_list_page.url)
        login_page.login()
    courses_list_page = CoursesListPage(page, login_page.url)
    courses_list_page.add_noo_course()
    courses_list_page.new_course_exist()
    yield
    coursers_list_page = CoursesListPage(page, courses_list_link)
    coursers_list_page.open()
    coursers_list_page.delete_file()

@allure.story("Общие тесты")
@allure.title("Проверка целостности таблицы")
def test_page_filtration(page):
    frp_page = FRPPage(page, link)
    frp_page.open()
    frp_page.ed_level_field_testing()
    frp_page.course_field_testing()
    frp_page.course_level_field_testing()