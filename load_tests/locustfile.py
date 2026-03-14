from locust import HttpUser, task, between


class ApiUser(HttpUser):
    """Симулирует пользователя, работающего с API"""

    host = "https://reqres.in"
    wait_time = between(1, 3)  # пауза между запросами 1-3 секунды

    @task(3)
    def get_users(self):
        """Получить список пользователей (наиболее частый запрос)"""
        self.client.get("/api/users", name="GET /users")

    @task(2)
    def get_single_user(self):
        """Получить одного пользователя"""
        self.client.get("/api/users/1", name="GET /users/:id")

    @task(1)
    def create_user(self):
        """Создать пользователя"""
        payload = {"name": "Load Test User", "job": "QA Engineer"}
        self.client.post("/api/users", json=payload, name="POST /users")
