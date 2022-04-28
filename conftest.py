import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from vars import CHROME_PATH


@pytest.fixture(scope='function')
def setup():
    # caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "eager"
    # driver = webdriver.Chrome(
    #     executable_path=CHROME_PATH,
    #     desired_capabilities=caps,
    #     options=options,
    # )
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    s = Service(executable_path=CHROME_PATH)
    driver = webdriver.Chrome(service=s, options=options)

    yield driver
    driver.quit()
