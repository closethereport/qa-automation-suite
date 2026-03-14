import pytest
import requests
import jsonschema

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "email", "first_name", "last_name", "avatar"],
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string", "format": "email"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"},
    },
}


def test_get_users_returns_200(api_base_url):
    """GET /users возвращает статус 200"""
    response = requests.get(f"{api_base_url}/users")
    assert response.status_code == 200


def test_get_users_returns_list(api_base_url):
    """GET /users возвращает список пользователей"""
    response = requests.get(f"{api_base_url}/users")
    data = response.json()
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0


def test_get_single_user_schema(api_base_url):
    """Схема ответа одного пользователя соответствует ожидаемой"""
    response = requests.get(f"{api_base_url}/users/1")
    user = response.json()["data"]
    jsonschema.validate(instance=user, schema=USER_SCHEMA)


def test_get_nonexistent_user_returns_404(api_base_url):
    """GET несуществующего пользователя возвращает 404"""
    response = requests.get(f"{api_base_url}/users/9999")
    assert response.status_code == 404


def test_create_user_returns_201(api_base_url):
    """POST /users создаёт пользователя и возвращает 201"""
    payload = {"name": "John Tester", "job": "QA Engineer"}
    response = requests.post(f"{api_base_url}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data


def test_update_user_returns_200(api_base_url):
    """PUT /users/:id обновляет данные пользователя"""
    payload = {"name": "Jane Tester", "job": "Senior QA"}
    response = requests.put(f"{api_base_url}/users/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]


def test_delete_user_returns_204(api_base_url):
    """DELETE /users/:id возвращает 204"""
    response = requests.delete(f"{api_base_url}/users/1")
    assert response.status_code == 204
