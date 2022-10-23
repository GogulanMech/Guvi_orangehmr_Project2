import allure
from base.page_base import PageBase


class PageTitle(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting Tittle of the page")
    def get_page_title(self):
        return self.driver.title




