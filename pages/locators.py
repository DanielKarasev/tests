import javaproperties, datetime

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class LoginPageLocators:
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#kc-login"

class BasePageLocators:
    CHECK_TEXT = ":text-is('Система управления сервисом')"

class BaseListPageLocators:
    ADD_BUTTON = "button > span:text-is('Добавить')"
    ID_COLUMN = "span.ant-table-column-title:text-is('ID')"
    NAME_COLUMN = "span.ant-table-column-title:text-is('Название')"
    BASE_NAME_COLUMN = "span.ant-table-column-title:text-is('Название документа-основания')"
    BASE_DATE_COLUMN = "span.ant-table-column-title:text-is('Дата документа-основания')"
    LINK_COLUMN = "span.ant-table-column-title:text-is('Ссылка')"
    ARCHIVE_COLUMN = "span.ant-table-column-title:text-is('В архиве')"
    DATE_COLUMN = "span.ant-table-column-title:text-is('Дата создания записи')"
    ADD_NAME_FIELD = "input[placeholder='Введите название']"
    ADD_BASE_NAME_FIELD = "input[placeholder='Введите согласованное название']"
    ADD_BASE_DATE_FIELD = "input[placeholder='Введите дату согласования']"
    ARCHIVE_CHECKBOX = "#isArchived[type='checkbox']"
    ADD_CONFIRM_BUTTON = "button > span:text-is('Сохранить')"
    ADD_PDF_BUTTON = 'input[type="file"]'
    ADD_NAME_ALERT = ".ant-form div:text-is('Обязательное поле')"
    ADD_BASE_DATE_ALERT = "div:text-is('Поле может содержать только дату')"
    ADD_PDF_ALERT = "div:text-is('Пожалуйста, прикрепите файл в формате PDF')"
    DELETE_BUTTON = "xpath=//table/tbody/tr[2]/*//*[name()='svg' and contains(@class, 'Delete_icon__')]"
    DELETE_CONFIRM_BUTTON = "button > span:text-is('Удалить')"
    EDIT_BUTTON = "xpath=//table/tbody/tr[2]/*//*[name()='svg' and contains(@class, 'Edit_icon__')]"
    date = (datetime.datetime.today() - datetime.timedelta(1)).strftime("%d.%m.%Y")
    BASE_DATE = f"div.ant-typography:text-is('{date}')"
    CLEAR_DATE_BUTTON = "span.ant-picker-clear"
    RECORD_NUMBERS = "li.ant-pagination-total-text"
    PAGE_ONE = "li > a:text-is('1')"
    PAGE_TWO = "li > a:text-is('2')"
    PAGE_BACK_BUTTON = "span:text-is('Назад')"
    PAGE_FORWARD_BUTTON = "span:text-is('Дальше')"

class FGOSListPageLocators:
    TEST_NAME = f"div.ant-typography:text-is('{props['fgos_test_name']}')"
    NEW_TEST_NAME = f"div.ant-typography:text-is('{props['new_fgos_test_name']}')"
    NEW_TEST_BASE_NAME = f"div.ant-typography:text-is('{props['new_fgos_test_base_name']}')"
    ADD_CANCEL_BUTTON = "button > span:text-is('Отмена')"

class FOOPListPageLocators:
    ADAPTED_COLUMN = "span.ant-table-column-title:text-is('Адаптирован')"
    ADAPTED_CHECKBOX = "#isAdapted[type='checkbox']"
    TEST_NAME = f"div.ant-typography:text-is('{props['foop_test_name']}')"
    TEST_BASE_NAME = f"div.ant-typography:text-is('{props['foop_test_base_name']}')"
    ADAPTED_CHECK = "xpath=//table/tbody/tr[2]/td[7]/div"
    ARCHIVE_CHECK = "xpath=//table/tbody/tr[2]/td[6]/div"
    NEW_TEST_NAME = f"div.ant-typography:text-is('{props['foop_new_test_name']}')"
    BASE_NAME = f"div.ant-typography:text-is('{props['foop_test_base_name']}')"
    NEW_TEST_BASE_NAME = f"div.ant-typography:text-is('{props['foop_new_test_base_name']}')"

class SanPINListPageLocators:
    TEST_NAME = f"div.ant-typography:text-is('{props['sanpin_test_name']}')"
    NEW_TEST_NAME = f"div.ant-typography:text-is('{props['sanpin_new_test_name']}')"
    BASE_NAME = f"div.ant-typography:text-is('{props['sanpin_test_base_name']}')"

class FGOSPageLocators:
    TEST_NAME = f"a:text-is('{props['fgos_test_name']}')"

class BaseSitePageLocators:
    ID_LINE = "div:text-is('ID')"
    NAME_LINE = "div:text-is('Название')"
    BASE_NAME_LINE = "div:text-is('Название документа-основания')"
    BASE_DATE_LINE = "div:text-is('Дата документа-основания')"
    LINK_LINE = "div:text-is('Файл')"
    ARCHIVE_LINE = "div:text-is('В архиве')"
    AUTOR_LINE = "div:text-is('Автор')"
    DATE_LINE = "div:text-is('Дата создания записи')"
    TEST_NAME = "div:text-is('Название') + div"
    TEST_BASE_NAME = "div:text-is('Название документа-основания') + div"
    AUTOR = "div:text-is('Автор') + div"
    ARCHIVE_CONDITION = "div:text-is('В архиве') + div"
    BASE_DATE = "div:text-is('Дата документа-основания') + div"
    FILE_NAME = "div:text-is('Файл') + div"
    DATE = "div:text-is('Дата создания записи') + div"

class FGOSSitePageLocators:
    ADD_FILE_BUTTON = "button > span:text-is('Создать')"
    ID_COLUMN = "span.ant-table-column-title:text-is('ID')"
    NAME_COLUMN = "span.ant-table-column-title:text-is('Название')"
    BASE_DATE_COLUMN = "span.ant-table-column-title:text-is('Дата документа-основания')"
    LINK_COLUMN = "span.ant-table-column-title:text-is('Ссылка')"
    DATE_COLUMN = "span.ant-table-column-title:text-is('Дата создания записи')"
    ADD_NAME_FIELD = "input[placeholder='Введите название']"
    ADD_BASE_DATE_FIELD = "input[placeholder='Введите дату согласования']"
    ADD_CONFIRM_BUTTON = "button > span:text-is('Сохранить')"
    ADD_PDF_BUTTON = 'input[type="file"]'
    ADD_NAME_ALERT = ".ant-form div:text-is('Обязательное поле')"
    ADD_BASE_DATE_ALERT = "div:text-is('Поле может содержать только дату')"
    ADD_PDF_ALERT = "div:text-is('Пожалуйста, прикрепите файл в формате PDF')"
    ADD_CANCEL_BUTTON = "button > span:text-is('Отмена')"
    NEW_FILE_NAME = f"div.ant-typography:text-is('{props['fgos_file_name']}')"
    DELETE_BUTTON = "svg[class*=Delete_icon]"
    DELETE_CONFIRM_BUTTON = "button > span:text-is('Удалить')"
    EDIT_BUTTON = "svg[class*=Edit_icon]"
    EDIT_FILE_NAME = f"div.ant-typography:text-is('{props['new_fgos_file_name']}')"
    NAME_FILTER_BUTTON = "svg[class*=FilterTable_icon]"
    NAME_FILTER_FIELD = "input[placeholder='Название']"
    NAME_FILTER_CONFIRM_BUTTON = "button > span:text-is('Поиск')"

class FGOSFilePageLocators:
    TEST_FILE_NAME = f"div:text-is('{props['fgos_file_name']}')"

class FGOSSiteFilePageLocators:
    ID_LINE = "div:text-is('ID')"
    NAME_LINE = "div:text-is('Название')"
    AUTOR_LINE = "div:text-is('Автор')"
    FILE_LINE = "div:text-is('Файл')"
    DATE_LINE = "div:text-is('Дата создания записи')"
    BASE_DATE_LINE = "div:text-is('Дата документа-основания')"
    NAME = "div:text-is('Название') + div"
    AUTOR = "div:text-is('Автор') + div"
    FILE_NAME = "div:text-is('Файл') + div"
    DATE = "div:text-is('Дата создания записи') + div"
    BASE_DATE = "div:text-is('Дата документа-основания') + div"

class FOOPPageLocators:
    TEST_NAME = f"a:text-is('{props['foop_test_name']}')"
    COUNT_100_BUTTON = "span:text-is('100')"
    BASE_FOOPS = "span:text-is('Основные')"
    ADAPTED_FOOPS = "span:text-is('Адаптированные')"

class FOOPSitePageLocators:
    ADAPTED_LINE = "div:text-is('Адаптирован')"
    ADAPTED_CONDITION = "div:text-is('Адаптирован') + div"

class SanPINPageLocators:
    TEST_NAME = f"a:text-is('{props['sanpin_test_name']}')"
    COUNT_100_BUTTON = "span:text-is('100')"