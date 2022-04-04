import abc
from typing import Optional

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: webdriver, url: str, timeout: int = 4) -> None:
        self.driver = driver
        self.url = url
        self.timeout = timeout
        self.driver.implicitly_wait(timeout)

    def _is_url_correct(self, expected_url: str):
        assert self.url.startswith(expected_url),\
            f'URL страницы должно начинаться с "{expected_url}", ' \
            f'но оно имеет значение {self.url=}'

    def open(self) -> None:
        self.driver.get(self.url)

    def is_element_present(self, how: By, what: str) -> bool:
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
