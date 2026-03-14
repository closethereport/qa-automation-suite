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
@pytest.mark.parametrize("username,password,expected_error", [
    ("standard_user", "wrong_password", "Username and password do not match"),
    ("", "", "Username is required"),
    ("locked_out_user", "secret_sauce", "locked out"),
])
def test_invalid_login(login_page, username, password, expected_error):
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()
