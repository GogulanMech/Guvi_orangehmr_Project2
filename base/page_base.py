import allure


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("opening main page")
    def open(self):
        self.driver.open()
