import time

import pytest
from pages.login_page import LogInPage
from pages.pim_001 import AddEmployee
import allure


@pytest.mark.usefixtures("setup")
class Test_PIM_03:

    @allure.title("Delete an exiting employee in the PIM module.")
    @allure.description("Search a employee in PIM module then delete that employee details ")
    def test_delete_employee(self):
        login_page = LogInPage(self.driver)
        add_emp = AddEmployee(self.driver)
        login_page.open()
        login_page.set_user_inputs("Admin", "admin123")
        add_emp.search_employee("gogul")
        add_emp.click_delete()
        validate = add_emp.set_validate()
        time.sleep(2)
        assert True if validate else False
        self.driver.quit()
