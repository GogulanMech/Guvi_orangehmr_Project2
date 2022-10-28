import time

import pytest
from pages.login_page import LogInPage
from pages.pim_001 import AddEmployee
from helpers.webdriver_listener import WebDriverListener
import allure


@pytest.mark.usefixtures("setup")
class Test_PIM_03:

    @allure.title("Delete an exiting employee in the PIM module.")
    @allure.description("Search a employee in PIM module then delete that employee details ")
    def test_delete_employee(self):
        login_page = LogInPage(self.driver)
        add_emp = AddEmployee(self.driver)
        logger = WebDriverListener()
        logger.logger.info("********Test_PIM_02********")
        logger.logger.info("********Open Orange HMR application********")
        login_page.open()
        logger.logger.info("********Login with user info********")
        login_page.set_user_inputs("Admin", "admin123")
        logger.logger.info("********Search existing employee********")
        add_emp.search_employee("gogul")
        logger.logger.info("********Delete existing employee********")
        add_emp.click_delete()
        validate = add_emp.set_validate()
        time.sleep(2)
        assert True if validate else False
        logger.logger.info("********Ending Test_PIM_03********")
        self.driver.quit()
