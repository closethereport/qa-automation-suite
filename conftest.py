import pytest
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="session")
def api_base_url():
    return os.getenv("API_BASE_URL", "https://reqres.in/api")


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("STANDARD_USER", "standard_user"),
        "password": os.getenv("PASSWORD", "secret_sauce"),
    }
