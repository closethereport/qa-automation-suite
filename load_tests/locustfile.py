from locust import HttpUser, task, between


class ApiUser(HttpUser):
    """Симулирует пользователя, работающего с API"""

    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)  # пауза между запросами 1-3 секунды

    @task(3)
    def get_users(self):
        """Получить список пользователей (наиболее частый запрос)"""
        self.client.get("/users", name="GET /users")

    @task(2)
    def get_single_user(self):
        """Получить одного пользователя"""
        self.client.get("/users/1", name="GET /users/:id")

    @task(1)
    def create_post(self):
        """Создать запись"""
        payload = {"title": "Load Test", "body": "test body", "userId": 1}
        self.client.post("/posts", json=payload, name="POST /posts")
