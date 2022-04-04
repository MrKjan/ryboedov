import os

import pytest as pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from vars import CHROME_PATH

@pytest.fixture(scope='function')
def setup():
    options = webdriver.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome(
        executable_path=CHROME_PATH,
        desired_capabilities=caps,
        options=options,
    )

    yield driver
    driver.quit()
