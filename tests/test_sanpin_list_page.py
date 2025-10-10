import pytest, allure, javaproperties
from pages.sanpin_list_page import SanPINListPage
from pages.sanpin_page import SanPINPage
from pages.login_page import LoginPage
#from pages.sanpin_site_page import SanPINSitePage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['sanpin_list_link']
site_link = props['sanpin_link']

@pytest.fixture(scope="function", autouse=True)
def setup(page):
    with allure.step('Логирование'):
        sanpin_list_page = SanPINListPage(page, link)
        sanpin_list_page.open()
        login_page = LoginPage(page, sanpin_list_page.url)
        login_page.login()

@allure.story("Общие тесты")
@allure.title("Проверка целостности таблицы")
def test_list_correct(page):
    with allure.step('Открытие страницы'):
        sanpin_list_page = SanPINListPage(page, link)
        sanpin_list_page.open()
    sanpin_list_page.base_list_correct()

@allure.story("Общие тесты")
@allure.title("Удаление записи")
def test_delete_file(page):
    with allure.step('Открытие страницы'):
        sanpin_list_page = SanPINListPage(page, link)
        sanpin_list_page.open()
    sanpin_list_page.add_full_file()
    sanpin_list_page.file_exist()
    sanpin_list_page.delete_file()
    sanpin_list_page.file_dont_exist()

@allure.story("Создание архивной нормы")
@allure.title("Попытка создать норму без имени")
def test_add_wrong_name_file(page):
    with allure.step('Открытие страницы'):
        sanpin_list_page = SanPINListPage(page, link)
        sanpin_list_page.open()
    sanpin_list_page.add_file_without_name()
    sanpin_list_page.file_dont_exist()

@allure.story("Создание архивной нормы")
@allure.title("Попытка создать норму без pdf файла")
def test_add_wrong_pdf_file(page):
    with allure.step('Открытие страницы'):
        sanpin_list_page = SanPINListPage(page, link)
        sanpin_list_page.open()
    sanpin_list_page.add_file_without_pdf()
    sanpin_list_page.file_dont_exist()

class TestsWithTraces():
    @pytest.fixture(scope="function", autouse=True)
    def teardown(self, page):
        yield
        sanpin_list_page = SanPINListPage(page, link)
        sanpin_list_page.open()
        sanpin_list_page.delete_file()
        sanpin_list_page.file_dont_exist()

    @allure.story("Создание архивной записи")
    @allure.title("Создание полной записи")
    def test_add_file(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_full_file()
        sanpin_list_page.file_exist()

    @allure.story("Редактирование записи")
    @allure.title("Изменение имени записи")
    def test_edit_file_name(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_full_file()
        sanpin_list_page.file_exist()
        sanpin_list_page.edit_file_name()
        sanpin_list_page.new_file_name_exist()

    @allure.story("Редактирование записи")
    @allure.title("Удаление названия документа-основания")
    def test_delete_file_base_name(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_full_file()
        sanpin_list_page.file_exist()
        sanpin_list_page.delete_file_base_name()
        sanpin_list_page.file_base_name_dont_exist()

    @allure.story("Редактирование записи")
    @allure.title("Удаление даты документа-основания")
    def test_delete_file_base_date(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_full_file()
        sanpin_list_page.file_exist()
        sanpin_list_page.delete_file_base_date()
        sanpin_list_page.file_base_date_dont_exist()

    @allure.story("Редактирование записи")
    @allure.title("Добавление названия документа-основания")
    def test_add_file_base_name(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_file_without_base_name()
        sanpin_list_page.file_exist()
        sanpin_list_page.file_base_name_dont_exist()
        sanpin_list_page.add_file_base_name()
        sanpin_list_page.base_name_exist()

    @allure.story("Редактирование записи")
    @allure.title("Добавление даты документа-основания")
    def test_add_file_base_date(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_file_without_base_date()
        sanpin_list_page.file_exist()
        sanpin_list_page.file_base_date_dont_exist()
        sanpin_list_page.add_file_base_date()
        sanpin_list_page.base_date_exist()

    @allure.story("Создание архивной записи")
    @allure.title("Создание записи без названия документа-основания")
    def test_add_file_without_base_name(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_file_without_base_name()
        sanpin_list_page.file_exist()

    @allure.story("Создание архивной записи")
    @allure.title("Создание записи без даты документа-основания")
    def test_add_file_without_base_date(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_file_without_base_date()
        sanpin_list_page.file_exist()

    @allure.story("Создание архивной записи")
    @allure.title("Создание записи без названия и даты документа-основания")
    def test_add_file_without_base_name_and_date(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_file_without_base_name_and_date()
        sanpin_list_page.file_exist()

    @allure.story("Создание неархивной записи")
    @allure.title("Создание полной записи")
    def test_add_unarchived_file(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_unarchived_file()
        sanpin_list_page.file_exist()
        sanpin_page = SanPINPage(page, site_link)
        sanpin_page.open()
        sanpin_page.new_file_exists()

    @allure.story("Создание неархивной записи без названия документа-основания")
    @allure.title("Создание полной записи")
    def test_add_unarchived_file_without_base_name(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_unarchived_file_without_base_name()
        sanpin_list_page.file_exist()
        sanpin_page = SanPINPage(page, site_link)
        sanpin_page.open()
        sanpin_page.new_file_exists()

    @allure.story("Создание неархивной записи без даты документа-основания")
    @allure.title("Создание полной записи")
    def test_add_unarchived_file_without_base_date(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_unarchived_file_without_base_date()
        sanpin_list_page.file_exist()
        sanpin_page = SanPINPage(page, site_link)
        sanpin_page.open()
        sanpin_page.new_file_exists()

    @allure.story("Создание неархивной записи без названия и даты документа основания")
    @allure.title("Создание полной записи")
    def test_add_unarchived_file_without_base_name_and_date(self, page):
        with allure.step('Открытие страницы'):
            sanpin_list_page = SanPINListPage(page, link)
            sanpin_list_page.open()
        sanpin_list_page.add_unarchived_file_without_base_name_and_date()
        sanpin_list_page.file_exist()
        sanpin_page = SanPINPage(page, site_link)
        sanpin_page.open()
        sanpin_page.new_file_exists()