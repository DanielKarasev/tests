import pytest, allure, javaproperties
from pages.login_page import LoginPage
from pages.base_list_page import BaseListPage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['base_list_link']

@pytest.fixture(scope="function", autouse=True)
def setup(page):
    with allure.step('Логирование'):
        base_list_page = BaseListPage(page, link)
        base_list_page.open()
        login_page = LoginPage(page, base_list_page.url)
        login_page.login()

@allure.story("Общие тесты")
@allure.title("Проверка пагитации №1")
def test_pagination_check_1(page):
    with allure.step('Открытие страницы'):
        base_list_page = BaseListPage(page, link)
        base_list_page.open()
    base_list_page.pagination_check_1()

@allure.story("Общие тесты")
@allure.title("Проверка пагитации №2")
def test_pagination_check_2(page):
    with allure.step('Открытие страницы'):
        base_list_page = BaseListPage(page, link)
        base_list_page.open()
    base_list_page.pagination_check_2()

@allure.story("Общие тесты")
@allure.title("Проверка пагитации №3")
def test_pagination_check_3(page):
    with allure.step('Открытие страницы'):
        base_list_page = BaseListPage(page, link)
        base_list_page.open()
    base_list_page.pagination_check_3()

@allure.story("Общие тесты")
@allure.title("Проверка пагитации №4")
def test_pagination_check_4(page):
    with allure.step('Открытие страницы'):
        base_list_page = BaseListPage(page, link)
        base_list_page.open()
    base_list_page.pagination_check_4()