import javaproperties, allure
from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators

class LoginPage(BasePage):
    def login(self):
        with allure.step('Вход'):
            username_field = self.page.locator(LoginPageLocators.USERNAME)
            password_field = self.page.locator(LoginPageLocators.PASSWORD)
            login_button = self.page.locator(LoginPageLocators.LOGIN_BUTTON)
            with open('../tests/data.properties', 'r', encoding='utf-8') as data:
                props = javaproperties.load(data)
                username = props['username']
                password = props['password']
                username_field.fill(username)
                password_field.fill(password)
                login_button.click()
            check_text = self.page.wait_for_selector(BasePageLocators.CHECK_TEXT, state='visible')