import pytest
from playwright.sync_api import Page
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.catalog_page import CatalogPage


@pytest.fixture
def catalog(page: Page, base_url, credentials):
    lp = LoginPage(page)
    lp.open(base_url)
    lp.login(credentials["username"], credentials["password"])
    return CatalogPage(page)


@pytest.mark.regression
def test_sort_by_name_az(catalog):
    catalog.sort_by("az")
    names = catalog.get_product_names()
    assert names == sorted(names)


@pytest.mark.regression
def test_sort_by_name_za(catalog):
    catalog.sort_by("za")
    names = catalog.get_product_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_sort_by_price_low_to_high(catalog):
    catalog.sort_by("lohi")
    prices = catalog.get_product_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_by_price_high_to_low(catalog):
    catalog.sort_by("hilo")
    prices = catalog.get_product_prices()
    assert prices == sorted(prices, reverse=True)
