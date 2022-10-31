from locators.locators import AddEmployeeLocators, E_PersonalLocators, AttachmentLocators, CommonLocator, Edit_Delete
import allure


class AddEmployee:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Clicking add employee")
    def click_add(self):
        self.driver.find_element(*AddEmployeeLocators.add_btn).click()

    @allure.step("Enter New Employee details")
    def set_employee_detail(self, fname, lname, id, img, username, passwrd):
        self.driver.find_element(*AddEmployeeLocators.fname_input).send_keys(fname)
        self.driver.find_element(*AddEmployeeLocators.lname_input).send_keys(lname)
        self.driver.find_element(*AddEmployeeLocators.eid_input).send_keys(id)
        self.driver.find_element(*AddEmployeeLocators.addimg_btn).send_keys(img)
        self.driver.find_element(*AddEmployeeLocators.logindetail_btn).click()
        self.driver.find_element(*AddEmployeeLocators.username_input).send_keys(username)
        self.driver.find_element(*AddEmployeeLocators.password_input).send_keys(passwrd)
        self.driver.find_element(*AddEmployeeLocators.confirmpass_input).send_keys(passwrd)
        self.driver.find_element(*AddEmployeeLocators.save_btn).click()

    @allure.step("Enter New Employee Personal details")
    def set_personal_details(self, otherid="123", licence="TN545664", date="2025-08-01", nationality="Indian",
                             status="Single", dob="1995-07-01", gender="Male"):
        self.driver.find_element(*E_PersonalLocators.otherid_input).send_keys(otherid)
        self.driver.find_element(*E_PersonalLocators.drivinglicens_input).send_keys(licence)
        self.driver.find_element(*E_PersonalLocators.expdate_input).send_keys(date)
        self.driver.find_element(*E_PersonalLocators.nationality_input).click()
        nationalities = self.driver.find_elements(*CommonLocator.dropdown_list)
        try:
            for n in nationalities:
                if n.text == nationality:
                    n.click()
                    break
        except:
            print(" Personal - Nationality  is invalid")

        self.driver.find_element(*E_PersonalLocators.maritalstatus_input).click()
        marital = self.driver.find_elements(*CommonLocator.dropdown_list)
        try:
            for s in marital:
                if s.text == status:
                    s.click()
                    break
        except:
            print(" Personal - Marital status  is invalid")

        self.driver.find_element(*E_PersonalLocators.dob_input).send_keys(dob)
        if gender == "Male" or gender == "male":
            male = self.driver.find_element(*E_PersonalLocators.male_input)
            self.driver.execute_script("arguments[0].click();", male)
        elif gender == "Female" or gender == "female":
            female = self.driver.find_element(*E_PersonalLocators.female_input)
            self.driver.execute_script("arguments[0].click();", female)
        else:
            self.driver.find_element(*E_PersonalLocators.male_input).click()

    def set_smoker(self, smoker=None):
        if smoker == "yes" or smoker == "Yes":
            yes = self.driver.find_element(*E_PersonalLocators.smokeryes_chkbox)
            self.driver.execute_script("arguments[0].click();", yes)
        else:
            pass

    def set_nickname(self, name="gogul"):
        self.driver.find_element(*E_PersonalLocators.nickname_input).send_keys(name)

    def set_ssn_sin_number(self, ssn="545664", sin="123456"):
        self.driver.find_element(*E_PersonalLocators.ssnnumber_input).send_keys(ssn)
        self.driver.find_element(*E_PersonalLocators.sinnumber_input).send_keys(sin)

    def set_military(self, number="5"):
        self.driver.find_element(*E_PersonalLocators.militaryservice_input).send_keys(number)

    @allure.step("Save the personal detail")
    def click_personal_save(self):
        save = self.driver.find_element(*E_PersonalLocators.save_btn)
        self.driver.execute_script("arguments[0].click();", save)

    @allure.step("Enter Blood Group detail")
    def set_blood_type(self, group="AB+"):
        self.driver.find_element(*E_PersonalLocators.bloodtype_btn).click()
        bloods = self.driver.find_elements(*CommonLocator.dropdown_list)
        for blood in bloods:
            if blood.text == group:
                blood.click()
                break
        save = self.driver.find_element(*E_PersonalLocators.customfieldsave_btn)
        self.driver.execute_script("arguments[0].click();", save)

    @allure.step("Enter personal attachment detail")
    def set_personal_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(*AttachmentLocators.attachment_btn).click()
        self.driver.find_element(*AttachmentLocators.selectfile_input).send_keys(file)
        self.driver.find_element(*AttachmentLocators.comment_input).send_keys(comment)
        self.driver.find_element(*AttachmentLocators.attachmentsave_btn).click()

    @allure.step("Validation is start")
    def set_validate(self):
        validate = self.driver.find_element(*CommonLocator.validate_txt).text
        return validate

    @allure.step("Search Employee by name")
    def search_employee(self, name):
        self.driver.find_element(*Edit_Delete.employee_name_input).send_keys(name)
        self.driver.find_element(*Edit_Delete.select_emp_drp).click()
        self.driver.find_element(*Edit_Delete.search_btn).click()

    @allure.step("Editing Existing Employee detail")
    def click_edit(self):
        self.driver.find_element(*Edit_Delete.edit_btn).click()

    @allure.step("Deleting Existing Employee")
    def click_delete(self):
        self.driver.find_element(*Edit_Delete.delete_btn).click()
        self.driver.find_element(*Edit_Delete.confirm_delete_btn).click()
