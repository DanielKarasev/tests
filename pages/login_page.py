import javaproperties, allure
from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators

with open('../tests/data.properties', 'r', encoding='utf-8') as data:
    props = javaproperties.load(data)

class LoginPage(BasePage):
    def login(self):
        with allure.step('Вход'):
            self.fill_field(LoginPageLocators.USERNAME, props['username'])
            self.fill_field(LoginPageLocators.PASSWORD, props['password'])
            login_button = self.page.locator(LoginPageLocators.LOGIN_BUTTON)
            login_button.click()
            check_text = self.page.wait_for_selector(BasePageLocators.CHECK_TEXT, state='visible')