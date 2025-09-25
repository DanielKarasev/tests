import pytest, allure, javaproperties
from pages.fgos_list_page import FGOSListPage
from pages.login_page import LoginPage
from pages.fgos_site_page import FGOSSitePage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['fgos_list_link']

@pytest.fixture(scope="function", autouse=True)
def setup(page):
    with allure.step('Логирование'):
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
        login_page = LoginPage(page, fgos_list_page.url)
        login_page.login()
        fgos_list_page = FGOSListPage(page, login_page.url)
    fgos_list_page.add_full_file()
    fgos_list_page.file_exist()
    #yield
    #fgos_list_page = FGOSListPage(page, link)
    #fgos_list_page.open()
    #fgos_list_page.delete_file()

@allure.story("Общие тесты")
@allure.title("Проверка целостности таблицы")
def test_table_correct(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.table_correct()

@allure.story("Добавление файла")
@allure.title("Добавление корректного файла")
def test_add_file(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file()
    fgos_site_page.new_fie_exist()