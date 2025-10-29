import pytest, allure, javaproperties
from pages.foop_list_page import FOOPListPage
from pages.foop_page import FOOPPage
from pages.login_page import LoginPage
from pages.foop_site_page import FOOPSitePage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['foop_list_link']
site_link = props['foop_link']

@pytest.fixture(scope="function", autouse=True)
def setup(page):
    with allure.step('Логирование'):
        foop_list_page = FOOPListPage(page, link)
        foop_list_page.open()
        login_page = LoginPage(page, foop_list_page.url)
        login_page.login()

@allure.story("Общие тесты")
@allure.title("Проверка целостности таблицы")
def test_list_correct(page):
    with allure.step('Открытие страницы'):
        foop_list_page = FOOPListPage(page, link)
        foop_list_page.open()
    foop_list_page.foop_list_correct()

@allure.story("Создание архивной неадаптированной записи")
@allure.title("Создание записи без имени")
def test_add_archive_unadapted_file_without_name(page):
    with allure.step('Открытие страницы'):
        foop_list_page = FOOPListPage(page, link)
        foop_list_page.open()
    foop_list_page.add_file_unadapted_without_name()
    foop_list_page.name_alert_correct()

@allure.story("Создание архивной адаптированной записи")
@allure.title("Создание записи без прикреплённого пдф файла")
def test_add_archive_adapted_file_without_pdf(page):
    with allure.step('Открытие страницы'):
        foop_list_page = FOOPListPage(page, link)
        foop_list_page.open()
    foop_list_page.add_file_unadapted_without_pdf()
    foop_list_page.pdf_alert_correct()

@allure.story("Изменения записи")
@allure.title("Удаление записи")
def test_delete_file(page):
    with allure.step('Открытие страницы'):
        foop_list_page = FOOPListPage(page, link)
        foop_list_page.open()
    foop_list_page.add_full_adapted_file()
    foop_list_page.file_exist()
    foop_list_page.delete_file()
    foop_list_page.file_dont_exist()

class TestsWithTrace():
    @pytest.fixture(scope="function", autouse=True)
    def teardown(self, page):
        yield
        foop_list_page = FOOPListPage(page, link)
        foop_list_page.open()
        foop_list_page.delete_file()

    @allure.story("Создание архивной адаптированной записи")
    @allure.title("Создание записи со всеми заполнеными полями")
    def test_add_archive_adapted_file(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_full_adapted_file()
        foop_list_page.file_exist()
        foop_list_page.true_adapted_check_test_correct()

    @allure.story("Создание архивной неадаптированной записи")
    @allure.title("Создание записи без названия документа основания")
    def test_add_archive_unadapted_file_without_base_name(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_file_unadapted_without_base_name()
        foop_list_page.file_exist()
        foop_list_page.false_adapted_check_test_correct()

    @allure.story("Создание архивной неадаптированной записи")
    @allure.title("Создание записи без даты документа основания")
    def test_add_archive_unadapted_file_without_base_date(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_file_unadapted_without_base_date()
        foop_list_page.file_exist()
        foop_list_page.false_adapted_check_test_correct()

    @allure.story("Создание архивной неадаптированной записи")
    @allure.title("Создание записи со всеми заполнеными полями")
    def test_add_archive_nonadapted_file(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_full_unadapted_file()
        foop_list_page.file_exist()
        foop_list_page.false_adapted_check_test_correct()

    @allure.story("Создание неархивной записи")
    @allure.title("Создание адаптированной записи")
    def test_add_adapted_file(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_adapted_unarchived_file()
        foop_list_page.file_exist()
        with allure.step('Открытие основного сайта'):
            foop_page = FOOPPage(page, site_link)
            foop_page.open()
        foop_page.adapted_testfile_exists()

    @allure.story("Создание неархивной записи")
    @allure.title("Создание неадаптированной записи")
    def test_add_nonadapted_file(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_unadapted_unarchived_file()
        foop_list_page.file_exist()
        with allure.step('Открытие основного сайта'):
            foop_page = FOOPPage(page, site_link)
            foop_page.open()
        foop_page.testfile_exists()

    @allure.story("Редактирование записи")
    @allure.title("Изменение имени записи")
    def test_edit_file_name(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_full_adapted_file()
        foop_list_page.file_exist()
        foop_list_page.edit_file_name()
        foop_list_page.new_file_name_exist()

    @allure.story("Редактирование записи")
    @allure.title("Изменение названия документа-основнаия")
    def test_edit_file_base_name(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_full_adapted_file()
        foop_list_page.file_exist()
        foop_list_page.edit_file_base_name()
        foop_list_page.new_file_base_name_exist()

    @allure.story("Редактирование записи")
    @allure.title("Удаление названия документа-основания")
    def test_delete_file_base_name(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_full_adapted_file()
        foop_list_page.file_exist()
        foop_list_page.delete_file_base_name()
        foop_list_page.base_name_didnt_exidt()

    @allure.story("Редактирование записи")
    @allure.title("Добавление названия документа-основания")
    def test_add_file_base_name(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_file_unadapted_without_base_name()
        foop_list_page.file_exist()
        foop_list_page.base_name_didnt_exidt()
        foop_list_page.add_file_base_name()
        foop_list_page.new_file_base_name_exist()

    @allure.story("Редактирование записи")
    @allure.title("Удаление даты документа основнаия")
    def test_delete_file_base_date(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_full_adapted_file()
        foop_list_page.file_exist()
        foop_list_page.delete_file_base_date()
        foop_list_page.base_date_didnt_exidt()

    @allure.story("Редактирование записи")
    @allure.title("Добавление даты документа-основания")
    def test_add_file_base_date(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_file_unadapted_without_base_date()
        foop_list_page.file_exist()
        foop_list_page.add_file_base_date()
        foop_list_page.base_date_exist()

    @allure.story("Общие тесты")
    @allure.title("Открытие записи в админке")
    def test_open_file_in_admin(self, page):
        with allure.step('Открытие страницы'):
            foop_list_page = FOOPListPage(page, link)
            foop_list_page.open()
        foop_list_page.add_full_adapted_file()
        foop_list_page.file_exist()
        foop_list_page.open_add_file()
        foop_site_page = FOOPSitePage(page, foop_list_page.url)
        foop_site_page.foop_page_exist()
        foop_site_page.foop_page_correct()