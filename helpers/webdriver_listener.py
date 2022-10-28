from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import AbstractEventListener
import logging
import datetime


class WebDriverListener(AbstractEventListener):
    log_filename = datetime.datetime.now().strftime("%y%m%d")
    logging.basicConfig(
        filename=f"{log_filename}.log",
        format="%(asctime)s: %(levelname)s: %(message)s",
        level=logging.INFO
    )

    def __init__(self):
        self.logger = logging.getLogger("selenium")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"{url} is opened")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")
        if by == 'xpath':
            element = driver.find_element(By.XPATH, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)
        elif by == 'name':
            element = driver.find_element(By.NAME, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)
        elif by == 'id':
            element = driver.find_element(By.ID, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)
        elif by == 'class name' or by == 'class_name':
            element = driver.find_element(By.CLASS_NAME, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)
        elif by == 'css selector':
            element = driver.find_element(By.CSS_SELECTOR, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)
        elif by == 'link text':
            element = driver.find_element(By.LINK_TEXT, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)
        elif by == 'partial link text':
            element = driver.find_element(By.PARTIAL_LINK_TEXT, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)
        elif by == 'tag name':
            element = driver.find_element(By.TAG_NAME, value)
            driver.execute_script("arguments[0].style.border='3px solid blue'", element)

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} was found")

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        pass
        # try:
        #     if element.get_attribute("text") is None:
        #         self.logger.info(f"{element.get_attribute('class')} was clicked")
        #     else:
        #         self.logger.info(f"{element.get_attribute('text')} was clicked")
        # except StaleElementReferenceException:
        #     if element.get_attribute("text") is None:
        #         self.logger.info(f"{element.get_attribute('class')} was clicked")
        #     else:
        #         self.logger.info(f"{element.get_attribute('text')} was clicked")

    def before_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} value is changing")

    def after_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} was changed")

    def before_quit(self, driver):
        self.logger.info("Driver is quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quited")

    def on_exception(self, exception, driver):
        self.logger.info(exception)























