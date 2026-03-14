import pytest
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    if request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        screenshot_path = f"reports/screenshots/{request.node.nodeid.replace('/', '_').replace('::', '_')}.png"
        page.screenshot(path=screenshot_path)


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
