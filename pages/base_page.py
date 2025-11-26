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
        file_name = self.page.wait_for_selector(what)
        file_name.click()

    def has_text(self, what, text):
        element = self.page.wait_for_selector(what)
        return element.inner_text() == text

    def fill_field(self, what, text):
        element = self.page.wait_for_selector(what)
        element.fill(text)