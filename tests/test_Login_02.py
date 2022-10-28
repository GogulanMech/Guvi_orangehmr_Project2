import allure
import pytest
from pages.login_page import LogInPage
from helpers.webdriver_listener import WebDriverListener


@pytest.mark.usefixtures("setup")
class Test_login_02:

    @allure.title("Login with invalid test data")
    @allure.description("This test of login with invalid data")
    def test_login(self):
        login_page = LogInPage(self.driver)
        logger = WebDriverListener()
        logger.logger.info("********Test_Login_02********")
        logger.logger.info("********Open Orange HMR application********")
        login_page.open()
        logger.logger.info("********Login with invalid data********")
        login_page.set_user_inputs("Admin", "dmin123")
        assert True if login_page.capture_msg() else False
        logger.logger.info("********Ending Test_Login_02********")
        self.driver.quit()


