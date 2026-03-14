import pytest
import os


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    if request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        screenshot_path = f"reports/screenshots/{request.node.nodeid.replace('/', '_').replace('::', '_')}.png"
        page.screenshot(path=screenshot_path)
