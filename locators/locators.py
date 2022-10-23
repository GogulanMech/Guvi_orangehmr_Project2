from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_input = (By.XPATH, "//input[@placeholder='Username']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    login_btn = (By.XPATH, "//button")
    invalid_data_msg = (By.XPATH, "//p[contains(text(),'Invalid credentials')]")


class AddEmployeeLocators:
    add_btn = (By.XPATH, "//button[normalize-space()='Add']")
    fname_input = (By.XPATH, "//input[@placeholder='First Name']")
    lname_input = (By.XPATH, "//input[@placeholder='Last Name']")
    eid_input = (By.XPATH, "//div[@class='oxd-grid-2 orangehrm-full-width-grid']//input[@class='oxd-input "
                           "oxd-input--active']")
    addimg_btn = (By.XPATH, "//input[@type='file']")
    logindetail_btn = (By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
    username_input = (By.XPATH, '//div[@class="oxd-form-row"]/child::div/descendant::input[@autocomplete="off"]')
    enable_btn = (By.XPATH, "//input[@value='1']")
    password_input = (By.XPATH, '//div[@class="oxd-grid-item oxd-grid-item--gutters user-password-cell"]//input['
                                '@type="password"]')
    confirmpass_input = (By.XPATH, '//div[@class="oxd-grid-item oxd-grid-item--gutters"]//input[@type="password"]')
    save_btn = (By.XPATH, "//button[@type='submit']")


class E_PersonalLocators:
    nickname_input = (By.XPATH, "//form[@class='oxd-form']/div[1]//input[@class='oxd-input oxd-input--active']")
    otherid_input = (By.XPATH, "//form[@class='oxd-form']/div[2]/div[1]/div[2]//input[@class='oxd-input "
                               "oxd-input--active']")
    drivinglicens_input = (By.XPATH, "//form[@class='oxd-form']/div[2]/div[2]/div[1]//input[@class='oxd-input "
                                     "oxd-input--active']")
    expdate_input = (By.XPATH, "//form[@class='oxd-form']/div[2]/div[2]/div[2]//input[@class='oxd-input "
                               "oxd-input--active']")
    ssnnumber_input = (By.XPATH, "//form[@class='oxd-form']/div[2]/div[3]/div[1]//input[@class='oxd-input "
                                 "oxd-input--active']")
    sinnumber_input = (By.XPATH, "//form[@class='oxd-form']/div[2]/div[3]/div[2]//input[@class='oxd-input "
                                 "oxd-input--active']")
    nationality_input = (By.XPATH, "//form[@class='oxd-form']/div[3]/div[1]/div[1]//i")
    maritalstatus_input = (By.XPATH, "//form[@class='oxd-form']/div[3]/div[1]/div[2]//i")
    dob_input = (
        By.XPATH, "//form[@class='oxd-form']/div[3]/div[2]/div[1]//input[@class='oxd-input oxd-input--active']")
    male_input = (By.XPATH, "//label/input[@value='1']")
    female_input = (By.XPATH, "//label/input[@value='2']")
    militaryservice_input = (By.XPATH, "//form[@class='oxd-form']/div[4]/div[1]/div[1]//input[@class='oxd-input "
                                       "oxd-input--active']")
    smokeryes_chkbox = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input["
                                  "@type='checkbox']")
    save_btn = (By.XPATH,
                "//form/div[5]//button[@type='submit']")  # its work only nickname present in page or DOM, otherwise use div[4]
    bloodtype_btn = (By.XPATH, "//div[@class='orangehrm-custom-fields']//i")
    customfieldsave_btn = (By.XPATH, "//form/div[2]//button[@type='submit']")


class VerificationLocators:
    toastcontainer_msg = (By.XPATH, '//div[@class="oxd-toast oxd-toast--error oxd-toast-container--toast"]')


class AttachmentLocators:
    attachment_btn = (By.XPATH, "//div[@class='orangehrm-action-header']/button[@type='button']")
    selectfile_input = (By.XPATH, "//input[@type='file']")
    comment_input = (By.TAG_NAME, "textarea")
    attachmentsave_btn = (By.XPATH, "//div[@class='oxd-form-actions']/button[2]")


class PimPageLocators:
    pimpage_link = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')
    employename_input = (By.XPATH, "//div[1]/div/div[2]/div/div/input[@placeholder='Type for hints...']")
    search_btn = (By.XPATH, "//button[@type='submit']")
    edit_btn = (By.XPATH, "//button/i[@class ='oxd-icon bi-pencil-fill']")
    delete_btn = (By.XPATH, "//button/i[@class='oxd-icon bi-trash']")
