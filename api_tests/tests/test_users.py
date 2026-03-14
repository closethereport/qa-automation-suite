import pytest
import requests
import jsonschema

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
}

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "body", "userId"],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"},
    },
}


@pytest.mark.smoke
def test_get_users_returns_200(api_base_url):
    response = requests.get(f"{api_base_url}/users")
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_users_returns_list(api_base_url):
    response = requests.get(f"{api_base_url}/users")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10


@pytest.mark.regression
def test_get_single_user_schema(api_base_url):
    response = requests.get(f"{api_base_url}/users/1")
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=USER_SCHEMA)


@pytest.mark.regression
def test_get_nonexistent_user_returns_404(api_base_url):
    response = requests.get(f"{api_base_url}/users/9999")
    assert response.status_code == 404


@pytest.mark.regression
def test_create_post_returns_201(api_base_url):
    payload = {"title": "QA Test Post", "body": "Automated test", "userId": 1}
    response = requests.post(f"{api_base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data


@pytest.mark.regression
def test_update_post_returns_200(api_base_url):
    payload = {"title": "Updated Title", "body": "Updated body", "userId": 1}
    response = requests.put(f"{api_base_url}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]


@pytest.mark.regression
def test_delete_post_returns_200(api_base_url):
    response = requests.delete(f"{api_base_url}/posts/1")
    assert response.status_code == 200
