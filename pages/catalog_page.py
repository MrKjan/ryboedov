from typing import Optional

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote import webelement

from pages.base_page import BasePage
from pages.locators import CatalogPageLocators
from robot.api.deco import keyword, library
from vars import HOME_LINK

LINK = HOME_LINK + '/catalog/'


@library
class CatalogPage(BasePage):
    def __init__(self, driver: webdriver, url: str) -> None:
        super().__init__(driver, url)

    @keyword
    def filter_by_descending(self, name: str) -> None:
        assert (price_filter := self.__get_price_filter_by_name(name=name)),\
            f'Невозможно фильтровать по {name=}'
        if self.__is_filter_active_order(name=name, ascending=False):
            return
        price_filter.click()
        if self.__is_filter_active_order(name=name, ascending=True):
            price_filter = self.__get_price_filter_by_name(name=name)
            price_filter.click()
        assert self.__is_filter_active_order(name=name, ascending=False),\
            f'Не получилось отфильтровать по {name=}'

    def __get_price_filter_by_name(
            self,
            name: str,
    ) -> Optional[webelement.WebElement]:
        filters = self.driver.find_elements(*CatalogPageLocators.SORT_BY)
        expected_filter = tuple(filter(
            lambda n: name.lower() == n.text.lower(),
            filters,
        ))
        if expected_filter:
            return expected_filter[0]
        return None

    def __is_filter_active_order(self, name: str, ascending: bool) -> bool:
        if ascending:
            flt = self.driver.find_element(
                *CatalogPageLocators.SORT_BY_ACTIVE_ASC,
            )
            if flt and flt.text == name:
                return True
            return False
        flt = self.driver.find_element(
            *CatalogPageLocators.SORT_BY_ACTIVE_DESC,
        )
        if flt and flt.text == name:
            return True
        return False

    def buy_item_by_order(self, number: int) -> None:
        buttons = self.driver.find_elements(
            *CatalogPageLocators.ACTIVE_BUY_BUTTON
        )
        assert len(buttons) >= number,\
            f'Доступных для покупки элементов меньше, чем {number=}'
        buttons[number].click()
        self.close_add_to_cart_popup()

    def close_add_to_cart_popup(self):
        assert (close := self.driver.find_element(
            *CatalogPageLocators.ADD_TO_CART_POPUP_CLOSE,
        )), 'Не появилось уведомление о добавлении в корзину'
        close.click()
