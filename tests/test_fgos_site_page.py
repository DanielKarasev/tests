import pytest, allure, javaproperties
from pages.fgos_list_page import FGOSListPage
from pages.fgos_site_file_page import FGOSSiteFilePage
from pages.login_page import LoginPage
from pages.fgos_site_page import FGOSSitePage
from pages.fgos_page import FGOSPage
from pages.fgos_file_page import FGOSFilePage

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
    yield
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.delete_file()

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
    fgos_site_page.new_file_exist()

@allure.story("Добавление файла")
@allure.title("Добавление файла без имени")
def test_add_file_without_name(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file_without_name()
    fgos_site_page.name_allert_correct()

@allure.story("Добавление файла")
@allure.title("Добавление файла без названия документа-основания")
def test_add_file_without_base_date(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file_without_base_date()
    fgos_site_page.base_date_allert_correct()

@allure.story("Добавление файла")
@allure.title("Добавление файла без pdf")
def test_add_file_without_pdf(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file_without_pdf()
    fgos_site_page.pdf_allert_correct()

@allure.story("Общие тесты")
@allure.title("Редактирование файла")
def test_edit_file(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file()
    fgos_site_page.new_file_exist()
    fgos_site_page.edit_file()
    fgos_site_page.new_file_name_exist()

@allure.story("Общие тесты")
@allure.title("Удаление файла")
def test_delete_file(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file()
    fgos_site_page.new_file_exist()
    fgos_site_page.delete_file()
    fgos_site_page.new_file_didnt_exist()

@allure.story("Общие тесты")
@allure.title("Поиск файла")
def test_find_file(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file()
    fgos_site_page.new_file_exist()
    fgos_site_page.edit_file()
    fgos_site_page.new_file_name_exist()
    fgos_site_page.add_file()
    fgos_site_page.new_file_exist()
    fgos_site_page.find_file(props['fgos_file_name'])
    fgos_site_page.new_file_exist()
    fgos_site_page.new_file_name_didnt_exist()
    fgos_site_page.find_file(props['new_fgos_file_name'])
    fgos_site_page.new_file_name_exist()
    fgos_site_page.new_file_didnt_exist()

@allure.story("Общие тесты")
@allure.title("Открытие файла")
def test_open_file(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file()
    fgos_site_page.new_file_exist()
    fgos_site_page.add_file_open()
    fgos_site_file_page = FGOSSiteFilePage(page, fgos_site_page.url)
    fgos_site_file_page.page_correct()

@allure.story("Добавление файла")
@allure.title("Добавление файла в неархивную запись")
def test_add_file_to_unarchive(page):
    fgos_list_page = FGOSListPage(page, link)
    fgos_list_page.open()
    fgos_list_page.delete_file()
    fgos_list_page.add_unarchived_file()
    fgos_list_page.open_add_file()
    fgos_site_page = FGOSSitePage(page, fgos_list_page.url)
    fgos_site_page.add_file()
    fgos_site_page.new_file_exist()
    fgos_page = FGOSPage(page, props['fgos_link'])
    fgos_page.open()
    fgos_page.new_file_exists()
    fgos_page.open_new_file()
    fgosfile_page = FGOSFilePage(page, fgos_page.url)
    fgosfile_page.tested_file_exist()