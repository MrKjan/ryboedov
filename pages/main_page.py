from typing import Optional

from selenium.webdriver.chrome import webdriver

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from vars import HOME_LINK

LINK = HOME_LINK


class MainPage(BasePage):
    def __init__(self, driver: webdriver, url: str) -> None:
        super().__init__(driver, url)

    def open(self) -> None:
        self.driver.get(self.url)

    def pick_catalog_from_page(self, name: str = None) -> None:
        catalogs = self.driver.find_elements(*MainPageLocators.CATALOG_NAME)
        found_catalog = tuple(filter(
            lambda n: name.lower() == n.text.lower(),
            catalogs,
        ))
        assert found_catalog, f'No catalogs matches {name=}'
        found_catalog[0].click()
