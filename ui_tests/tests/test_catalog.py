import pytest
from playwright.sync_api import Page
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.catalog_page import CatalogPage
from ui_tests.pages.cart_page import CartPage


@pytest.fixture
def logged_in_catalog(page: Page, base_url, credentials):
    lp = LoginPage(page)
    lp.open(base_url)
    lp.login(credentials["username"], credentials["password"])
    return CatalogPage(page)


@pytest.mark.smoke
def test_catalog_shows_products(logged_in_catalog):
    count = logged_in_catalog.get_product_count()
    assert count == 6


@pytest.mark.smoke
def test_add_product_to_cart(logged_in_catalog):
    logged_in_catalog.add_first_product_to_cart()
    assert logged_in_catalog.get_cart_count() == "1"


@pytest.mark.regression
def test_go_to_cart_after_adding(logged_in_catalog):
    logged_in_catalog.add_first_product_to_cart()
    logged_in_catalog.go_to_cart()
    cart = CartPage(logged_in_catalog.page)
    assert cart.get_item_count() == 1
