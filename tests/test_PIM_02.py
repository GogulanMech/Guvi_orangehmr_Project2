import pytest
from pages.login_page import LogInPage
from pages.pim_001 import AddEmployee
from helpers.webdriver_listener import WebDriverListener
import allure


@pytest.mark.usefixtures("setup")
class Test_PIM_02:

    @allure.title("Edit an exiting employee in the PIM module.")
    @allure.description("Search a employee in PIM module then Edit that employee details ")
    def test_edit_employee(self):
        login_page = LogInPage(self.driver)
        add_emp = AddEmployee(self.driver)
        logger = WebDriverListener()
        logger.logger.info("********Test_PIM_02********")
        login_page.set_user_inputs("Admin", "admin123")
        logger.logger.info("********Search existing employee********")
        add_emp.search_employee("gogul")
        logger.logger.info("********Edit existing employee details********")
        add_emp.click_edit()
        add_emp.set_blood_type("A+")
        validate = add_emp.set_validate()
        assert True if validate else False
        logger.logger.info("********Ending Test_PIM_02********")
        self.driver.quit()


