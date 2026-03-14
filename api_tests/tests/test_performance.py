import pytest

MAX_RESPONSE_TIME = 2.0


@pytest.mark.regression
@pytest.mark.parametrize("path", ["/users", "/users/1", "/posts", "/posts/1"])
def test_response_time(api_client, path):
    response = api_client.get(path)
    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME
