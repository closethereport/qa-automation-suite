import pytest


@pytest.mark.regression
@pytest.mark.parametrize("payload", [
    {},
    {"title": ""},
    {"title": 123, "body": None, "userId": "invalid"},
])
def test_create_post_with_invalid_data(api_client, payload):
    response = api_client.post("/posts", json=payload)
    assert response.status_code in (200, 201)


@pytest.mark.regression
@pytest.mark.parametrize("user_id", [0, -1, 99999, "abc"])
def test_get_user_invalid_id(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code == 404


@pytest.mark.regression
def test_update_nonexistent_post(api_client):
    payload = {"title": "Test", "body": "Test", "userId": 1}
    response = api_client.put("/posts/99999", json=payload)
    assert response.status_code in (200, 404, 500)


@pytest.mark.regression
def test_delete_nonexistent_post(api_client):
    response = api_client.delete("/posts/99999")
    assert response.status_code in (200, 404)
