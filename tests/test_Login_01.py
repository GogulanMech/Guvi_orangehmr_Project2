import allure
import pytest
from pages.login_page import LogInPage
from pages.page_title import PageTitle
from helpers.webdriver_listener import WebDriverListener


@pytest.mark.usefixtures("setup")
class Test_login_01:

    @allure.title("Login with valid test data")
    @allure.description("This test of login with valid data")
    def test_login(self):
        login_page = LogInPage(self.driver)
        page_title = PageTitle(self.driver)
        logger = WebDriverListener()
        logger.logger.info("********Test_Login_01********")
        logger.logger.info("********Open Orange HMR application********")
        login_page.open()
        logger.logger.info("********Login with user info********")
        login_page.set_user_inputs("Admin", "admin123")
        exp_title = "OrangeHRM"
        print(page_title.get_page_title)
        assert True if exp_title == page_title.get_page_title() else False
        logger.logger.info("********Ending Test_Login_01********")
        self.driver.quit()



