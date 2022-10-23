import json
import allure
import pytest
from allure_commons.types import AttachmentType
from utilities.driver_factory import DriverFactory

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSER = ["chrome", "firebox", "edge"]
DEFAULT_URL = "https://opensource-demo.orangehrmlive.com/"


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope='session')
def browser_setup(config):
    if "browser" not in config:
        raise Exception("The config file dose not contain 'browser' ")
    elif config["browser"] not in SUPPORTED_BROWSER:
        raise Exception(f'{config["browser"]} is not  a supported browser')
    return config["browser"]


@pytest.fixture(scope="session")
def wait_time_setup(config):
    return config["timeout"] if "timeout" in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope="session")
def url_setup(config):
    return config["base_url"] if "base_url" in config else DEFAULT_URL


@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Test_failed", attachment_type=AttachmentType.PNG)
        driver.quit()





















