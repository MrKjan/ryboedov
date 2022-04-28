from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from vars import HOME_LINK


def test_buy_two_items(
    setup
) -> None:
    driver = setup
    main_page = MainPage(driver, HOME_LINK)
    main_page.open()
    main_page.pick_catalog_from_page(name='Рыба')
    catalog_page = CatalogPage(driver, driver.current_url)
    catalog_page.filter_by_descending(name='Цене')
    catalog_page.buy_item_by_order(number=0)
    catalog_page.buy_item_by_order(number=1)
