import allure
import pytest
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup")
class Test_login_02:

    @allure.title("Login with invalid test data")
    @allure.description("This test of login with invalid data")
    def test_login(self):
        login_page = LogInPage(self.driver)
        login_page.open()
        login_page.set_user_inputs("Admin", "dmin123")
        assert True if login_page.capture_msg() else False
        self.driver.quit()


