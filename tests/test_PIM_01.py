import time

import pytest
import allure
from pages.login_page import LogInPage
from pages.pim_001 import AddEmployee


@pytest.mark.usefixtures("setup")
class Test_PIM_001:

    @allure.title("Add a new employee in the PIM module.")
    @allure.description("Add a new employee details and personal detail of the employee ")
    def test_add_employee(self):
        login_page = LogInPage(self.driver)
        add_emp = AddEmployee(self.driver)
        path = "D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work\\Project2\\test-data\\gogul_photo.jpg"
        login_page.open()
        self.driver.implicitly_wait(10)
        login_page.set_user_inputs("Admin", "admin123")
        status = []
        add_emp.click_add()
        add_emp.set_employee_detail("Gogulan", "M", "0215", path, "gogulan", "Gogulan@123")
        validate = add_emp.set_validate()
        status.append(True) if "Success" in validate else status.append(False)
        add_emp.set_personal_details("0125", "Tn123456", "2026-04-01", "Indian", "Single", "1995-07-01", "Male")
        add_emp.set_smoker("yes")
        add_emp.set_nickname("mech")
        add_emp.set_ssn_sin_number("354645", "4654656")
        add_emp.click_personal_save()
        validate = add_emp.set_validate()
        status.append(True) if "Success" in validate else status.append(False)
        add_emp.set_blood_type("AB+")
        time.sleep(2)
        validate = add_emp.set_validate()
        status.append(True) if "Success" in validate else status.append(False)
        add_emp.set_personal_attachment(path, "welcome")
        time.sleep(2)
        validate = add_emp.set_validate()
        status.append(True) if "Success" in validate else status.append(False)
        assert True if False not in status else False
        self.driver.quit()

