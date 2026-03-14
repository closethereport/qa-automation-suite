import pytest
from playwright.sync_api import Page
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.catalog_page import CatalogPage


@pytest.fixture
def login_page(page: Page, base_url):
    lp = LoginPage(page)
    lp.open(base_url)
    return lp


@pytest.mark.smoke
def test_successful_login(login_page, credentials):
    login_page.login(credentials["username"], credentials["password"])
    assert login_page.page.url.endswith("/inventory.html")


@pytest.mark.regression
def test_login_with_wrong_password(login_page):
    login_page.login("standard_user", "wrong_password")
    error = login_page.get_error_message()
    assert "Username and password do not match" in error


@pytest.mark.regression
def test_login_with_empty_fields(login_page):
    login_page.login("", "")
    error = login_page.get_error_message()
    assert "Username is required" in error


@pytest.mark.regression
def test_locked_user_cannot_login(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.get_error_message()
    assert "locked out" in error
