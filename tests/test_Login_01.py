import allure
import pytest
from pages.login_page import LoginPage
from pages.page_title import PageTitle


@pytest.mark.usefixtures("setup")
class Test_login_01:

    @allure.title("Login with valid test data")
    @allure.description("This test of login with valid data")
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.set_user_inputs("Admin", "admin123")
        exp_title = "OrangeHRM"
        print(PageTitle.get_page_title)
        assert True if exp_title == PageTitle.get_page_title else False


