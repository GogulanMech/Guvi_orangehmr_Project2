import allure
from locators.locators import LoginPageLocators
from base.page_base import PageBase


class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Login with username and password")
    def set_user_inputs(self, username, password):
        self.driver.find_element(*LoginPageLocators.username_input).send_keys(username)
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(password)
        self.driver.find_element(*LoginPageLocators.login_btn).click()
