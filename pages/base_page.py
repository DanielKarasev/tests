import allure
from playwright.sync_api import Page, expect
from .locators import BasePageLocators

class BasePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def is_element_present(self, what):
        element = self.page.wait_for_selector(what)
        return element.is_visible()

    def is_not_element_present(self, what):
        element = self.page.locator(what)
        expect(element).not_to_be_attached()

    def open_file(self, what):
        file_name = self.page.locator(what)
        file_name.click()

#    def page_switch_to_one(self):
#        with allure.step('Переключение на первую страницу'):
#            page_switch = self.page.locator(BasePageLocators.PAGE_ONE)
#            page_switch.click()

#    def page_switch_to_two(self):
#        with allure.step('Переключение на вторую страницу'):
#            page_switch = self.page.locator(BasePageLocators.PAGE_TWO)
#            page_switch.click()

#    def page_switch_to_next(self):
#        with allure.step('Переключение на следующую страницу'):
#            page_switch = self.page.locator(BasePageLocators.PAGE_FORWARD_BUTTON)
#            page_switch.click()

#    def page_switch_to_back(self):
#        with allure.step('Переключение на предыдущую страницу'):
#            page_switch = self.page.locator(BasePageLocators.PAGE_BACK_BUTTON)
#            page_switch.click()

#    def checking_record_numbers(self):
#        with allure.step('Проверка того какие записи на странице'):
#            numbers = self.page.locator(BasePageLocators.RECORD_NUMBERS)
#            return numbers.inner_text()

#   def pagination_check_1(self):
#        num_page_one = self.checking_record_numbers()
#        self.page_switch_to_two()
#        num_page_two = self.checking_record_numbers()
#        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
#            assert num_page_one != num_page_two

#    def pagination_check_2(self):
#        num_page_one = self.checking_record_numbers()
#        self.page_switch_to_next()
#        num_page_two = self.checking_record_numbers()
#        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
#            assert num_page_one != num_page_two

#    def pagination_check_3(self):
#        self.page_switch_to_next()
#        num_page_one = self.checking_record_numbers()
#        self.page_switch_to_one()
#        num_page_two = self.checking_record_numbers()
#        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
#            assert num_page_one != num_page_two

#    def pagination_check_4(self):
#        self.page_switch_to_two()
#        num_page_one = self.checking_record_numbers()
#        self.page_switch_to_back()
#        num_page_two = self.checking_record_numbers()
#        with allure.step('Сверка того что записи на 1 и 2 страницах разные'):
#            assert num_page_one != num_page_two