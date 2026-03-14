import pytest
from playwright.sync_api import Page
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.catalog_page import CatalogPage
from ui_tests.pages.cart_page import CartPage
from ui_tests.pages.checkout_page import CheckoutPage


@pytest.fixture
def checkout_page(page: Page, base_url, credentials):
    lp = LoginPage(page)
    lp.open(base_url)
    lp.login(credentials["username"], credentials["password"])
    catalog = CatalogPage(page)
    catalog.add_first_product_to_cart()
    catalog.go_to_cart()
    cart = CartPage(page)
    cart.proceed_to_checkout()
    return CheckoutPage(page)


def test_checkout_complete(checkout_page):
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.continue_to_overview()
    checkout_page.finish_order()
    assert checkout_page.get_complete_message() == "Thank you for your order!"


def test_checkout_without_info_shows_error(checkout_page):
    checkout_page.continue_to_overview()
    error = checkout_page.page.locator("[data-test='error']")
    assert error.is_visible()
