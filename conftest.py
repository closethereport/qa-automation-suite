import pytest
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="session")
def api_base_url():
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("STANDARD_USER", "standard_user"),
        "password": os.getenv("PASSWORD", "secret_sauce"),
    }
