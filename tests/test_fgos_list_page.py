import pytest, allure, javaproperties
from pages.fgos_list_page import FGOSListPage
from pages.login_page import LoginPage

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


@allure.title("Проверка целостности таблицы")
def test_list_correct(page):
    with allure.step('Открытие страницы'):
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
    fgos_list_page.base_list_correct()

@allure.story("Редактирование записи")
@allure.title("Удаление записи")
def test_delete_file(page):
    with allure.step('Открытие страницы'):
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
    fgos_list_page.add_full_file()
    fgos_list_page.file_exist()
    fgos_list_page.delete_file()
    fgos_list_page.file_dont_exist()

@allure.story("Создание архивной записи")
@allure.title("Создание записи без названия")
def test_add_file_without_name(page):
    with allure.step('Открытие страницы'):
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
    fgos_list_page.add_file_without_name()
    fgos_list_page.name_alert_correct()

@allure.story("Создание архивной записи")
@allure.title("Создание записи без названия документа-основания")
def test_add_file_without_base_name(page):
    with allure.step('Открытие страницы'):
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
    fgos_list_page.add_file_without_base_name()
    fgos_list_page.name_alert_correct()

@allure.story("Создание архивной записи")
@allure.title("Создание записи без даты документа основания")
def test_add_file_without_base_date(page):
    with allure.step('Открытие страницы'):
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
    fgos_list_page.add_file_without_base_date()
    fgos_list_page.date_alert_correct()

@allure.story("Создание архивной записи")
@allure.title("Создание записи без pdf файла")
def test_add_file_without_pdf(page):
    with allure.step('Открытие страницы'):
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
        fgos_list_page.add_file_without_pdf()
        fgos_list_page.pdf_alert_correct()

class TestsWithTraces():
    @pytest.fixture(scope="function", autouse=True)
    def teardown(self, page):
        yield
        fgos_list_page = FGOSListPage(page, link)
        fgos_list_page.open()
        fgos_list_page.delete_file()
        fgos_list_page.file_dont_exist()

    @allure.story("Создание архивной записи")
    @allure.title("Создание полной записи")
    def test_add_file(self, page):
        with allure.step('Открытие страницы'):
            fgos_list_page = FGOSListPage(page, link)
            fgos_list_page.open()
        fgos_list_page.add_full_file()
        fgos_list_page.file_exist()

    @allure.story("Редактирование записи")
    @allure.title("Изменение имени записи")
    def test_edit_file_name(self, page):
        with allure.step('Открытие страницы'):
            fgos_list_page = FGOSListPage(page, link)
            fgos_list_page.open()
        fgos_list_page.add_full_file()
        fgos_list_page.file_exist()
        fgos_list_page.edit_file_name()
        fgos_list_page.new_file_exist()