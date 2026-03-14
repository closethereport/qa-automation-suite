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


def test_get_users_returns_200(api_base_url):
    """GET /users возвращает статус 200"""
    response = requests.get(f"{api_base_url}/users")
    assert response.status_code == 200


def test_get_users_returns_list(api_base_url):
    """GET /users возвращает список из 10 пользователей"""
    response = requests.get(f"{api_base_url}/users")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10


def test_get_single_user_schema(api_base_url):
    """Схема ответа одного пользователя соответствует ожидаемой"""
    response = requests.get(f"{api_base_url}/users/1")
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=USER_SCHEMA)


def test_get_nonexistent_user_returns_404(api_base_url):
    """GET несуществующего пользователя возвращает 404"""
    response = requests.get(f"{api_base_url}/users/9999")
    assert response.status_code == 404


def test_create_post_returns_201(api_base_url):
    """POST /posts создаёт запись и возвращает 201"""
    payload = {"title": "QA Test Post", "body": "Automated test", "userId": 1}
    response = requests.post(f"{api_base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data


def test_update_post_returns_200(api_base_url):
    """PUT /posts/:id обновляет запись и возвращает 200"""
    payload = {"title": "Updated Title", "body": "Updated body", "userId": 1}
    response = requests.put(f"{api_base_url}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]


def test_delete_post_returns_200(api_base_url):
    """DELETE /posts/:id возвращает 200"""
    response = requests.delete(f"{api_base_url}/posts/1")
    assert response.status_code == 200
