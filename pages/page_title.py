import allure
from selenium.webdriver.common.by import By

from base.page_base import PageBase


class PageTitle(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting Tittle of the page")
    def get_page_logo(self):
        return self.driver.find_element(By.XPATH, "//div[@class='oxd-brand-banner']").is_displayed()




