from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOG_NAME = (
        By.CSS_SELECTOR,
        '.catalog-sections .catalog-section-title span',
    )


class CatalogPageLocators:
    SORT_BY = (
        By.CSS_SELECTOR,
        '.sort-by-options a'
    )
    SORT_BY_ACTIVE_DESC = (
        By.CSS_SELECTOR,
        '.sort-by-options .active.desc a',
    )
    SORT_BY_ACTIVE_ASC = (
        By.CSS_SELECTOR,
        '.sort-by-options .active.asc a',
    )
    ACTIVE_BUY_BUTTON = (
        By.CSS_SELECTOR,
        '.catalog-items .catalog-item>.catalog-item-price-and-buy a[data-action="add-to-basket"]'
    )
    ADD_TO_CART_POPUP_TEXT = (
        By.CSS_SELECTOR,
        '.item-added-action-title'
    )
    ADD_TO_CART_POPUP_CLOSE = (
        By.CSS_SELECTOR,
        '.fancybox-close'
    )
