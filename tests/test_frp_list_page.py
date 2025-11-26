import pytest, allure, javaproperties
from pages.frp_list_page import FRPListPage
from pages.courses_list_page import CoursesListPage
from pages.frp_page import FRPPage
from pages.frp_site_page import FRPSitePage
from pages.login_page import LoginPage

with open('data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

link = props['frp_list_link']
site_link = props['frp_link']
courses_link = props['courses_list_link']

@pytest.fixture(scope="function", autouse=True)
def setup(page):
    with allure.step('Логирование'):
        frp_list_page = FRPListPage(page, link)
        frp_list_page.open()
        login_page = LoginPage(page, frp_list_page.url)
        login_page.login()

@allure.story("Общие тесты")
@allure.title("Проверка целостности таблицы")
def test_list_correct(page):
    with allure.step('Открытие страницы'):
        frp_list_page = FRPListPage(page, link)
        frp_list_page.open()
    frp_list_page.frp_list_correct()

class TestsWithSubjects():
    @pytest.fixture(scope="function", autouse=True)
    def sub_setup(self, page):
        with allure.step('Добавление тестового предмета'):
            courses_list_page = CoursesListPage(page, courses_link)
            courses_list_page.open()
            courses_list_page.add_noo_course()
            courses_list_page.new_course_exist()
        yield
        with allure.step('Удаление тестового предмета'):
            coursers_list_page = CoursesListPage(page, courses_link)
            coursers_list_page.open()
            coursers_list_page.delete_file()

    @allure.story("Добавление записи")
    @allure.title("Добавление архивной базовой записи без имени")
    def test_add_archive_base_file_without_name(self, page):
        with allure.step('Открытие страницы'):
            frp_list_page = FRPListPage(page, link)
            frp_list_page.open()
        frp_list_page.add_archive_base_file_without_name()
        frp_list_page.name_alert_correct()

    @allure.story("Добавление записи")
    @allure.title("Добавление архивной базовой записи без курса")
    def test_add_archive_base_file_without_course(self, page):
        with allure.step('Открытие страницы'):
            frp_list_page = FRPListPage(page, link)
            frp_list_page.open()
        frp_list_page.add_archive_base_file_without_course()
        frp_list_page.name_alert_correct()

    @allure.story("Добавление записи")
    @allure.title("Добавление архивной базовой записи без pdf файла")
    def test_add_archive_base_file_without_pdf(self, page):
        with allure.step('Открытие страницы'):
            frp_list_page = FRPListPage(page, link)
            frp_list_page.open()
        frp_list_page.add_archive_base_file_without_pdf()
        frp_list_page.name_alert_correct()

    @allure.story("Общие тесты")
    @allure.title("Удаление записи")
    def test_delete_file(self, page):
        with allure.step('Открытие страницы'):
            frp_list_page = FRPListPage(page, link)
            frp_list_page.open()
        frp_list_page.add_full_archive_base_file()
        frp_list_page.file_exist()
        frp_list_page.delete_file()
        frp_list_page.file_not_exist()

    class TestsWithTrails():
        @pytest.fixture(scope="function", autouse=True)
        def teardown(self, page):
            yield
            with allure.step('Удаление тестовой записи'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
                frp_list_page.delete_file()

        @allure.story("Добавление записи")
        @allure.title("Добавление архивной базовой записи")
        def test_add_full_archive_base_file(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_full_archive_base_file()
            frp_list_page.file_exist()
            frp_list_page.base_status_true()

        @allure.story("Добавление записи")
        @allure.title("Добавление архивной базовой записи без названия документа-оснвования")
        def test_add_archive_base_file_without_base_name(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_archive_base_file_without_base_name()
            frp_list_page.file_exist()
            frp_list_page.base_name_didnt_exist()

        @allure.story("Добавление записи")
        @allure.title("Добавление архивной базовой записи без даты документа-оснвования")
        def test_add_archive_base_file_without_base_date(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_archive_base_file_without_base_date()
            frp_list_page.file_exist()
            frp_list_page.base_date_didnt_exist()

        @allure.story("Добавление записи")
        @allure.title("Добавление архивной базовой записи без названия и даты документа-оснвования")
        def test_add_archive_base_file_without_base_name_and_date(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_archive_base_file_without_base_name_and_date()
            frp_list_page.file_exist()
            frp_list_page.base_name_didnt_exist()
            frp_list_page.base_date_didnt_exist()

        @allure.story("Добавление записи")
        @allure.title("Добавление архивной небазовой записи")
        def test_add_archive_full_file(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_archive_full_file()
            frp_list_page.file_exist()
            frp_list_page.base_status_false()

        @allure.story("Добавление записи")
        @allure.title("Добавление неархивной базовой записи")
        def test_add_full_base_file(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_full_base_file()
            frp_list_page.file_exist()
            frp_page = FRPPage(page, site_link)
            frp_page.open()
            frp_page.testfile_exists()

        @allure.story("Изменение записи")
        @allure.title("Изменение имени записи")
        def test_edit_file_name(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_full_archive_base_file()
            frp_list_page.file_exist()
            frp_list_page.edit_file_name()
            frp_list_page.changed_name_exist()

        @allure.story("Изменение записи")
        @allure.title("Изменение нахвания документа-основания")
        def test_edit_file_base_name(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_full_archive_base_file()
            frp_list_page.file_exist()
            frp_list_page.edit_base_name()
            frp_list_page.changed_base_name_exist()

        @allure.story("Изменение записи")
        @allure.title("Добавление названия документа-основания в запись где его изначально не было")
        def test_add_base_name(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_archive_base_file_without_base_name()
            frp_list_page.file_exist()
            frp_list_page.base_name_didnt_exist()
            frp_list_page.edit_add_base_name()
            frp_list_page.base_name_exist()

        @allure.story("Изменение записи")
        @allure.title("Добавление даты документа-основания в запись где её изначально не было")
        def test_add_base_date(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_archive_base_file_without_base_date()
            frp_list_page.file_exist()
            frp_list_page.edit_add_base_date()

        @allure.story("Изменение записи")
        @allure.title("Удаление названия документа-основания из записи")
        def test_delete_base_name(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_full_archive_base_file()
            frp_list_page.file_exist()
            frp_list_page.delete_file_base_name()
            frp_list_page.base_name_didnt_exist()

        @allure.story("Изменение записи")
        @allure.title("Удаление даты документа-основания из записи")
        def test_delete_base_date(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_full_archive_base_file()
            frp_list_page.file_exist()
            frp_list_page.delete_file_base_date()
            frp_list_page.base_date_didnt_exist()

        @allure.story("Общие тесты")
        @allure.title("Открытие записи")
        def test_open_file(self, page):
            with allure.step('Открытие страницы'):
                frp_list_page = FRPListPage(page, link)
                frp_list_page.open()
            frp_list_page.add_full_archive_base_file()
            frp_list_page.file_exist()
            frp_list_page.base_status_true()
            frp_list_page.open_frp_file()
            frp_site_page = FRPSitePage(page, frp_list_page.url)
            frp_site_page.frp_page_exist()
            frp_site_page.frp_page_correct()

        class TestWithAdditionalCourse():
            @pytest.fixture(scope="function", autouse=True)
            def additional_setup(self, page):
                with allure.step('Добавление второго тестового предмета'):
                    courses_list_page = CoursesListPage(page, courses_link)
                    courses_list_page.open()
                    courses_list_page.add_changed_ooo_course()
                    courses_list_page.changed_course_exist()
                yield
                with allure.step('Удаление тестового предмета'):
                    coursers_list_page = CoursesListPage(page, courses_link)
                    coursers_list_page.open()
                    coursers_list_page.delete_file()

            @allure.story("Изменение записи")
            @allure.title("Изменение предмета")
            def test_edit_course(self, page):
                with allure.step('Открытие страницы'):
                    frp_list_page = FRPListPage(page, link)
                    frp_list_page.open()
                frp_list_page.add_full_archive_base_file()
                frp_list_page.file_exist()
                frp_list_page.change_course()
                frp_list_page.changed_course_name_exist()