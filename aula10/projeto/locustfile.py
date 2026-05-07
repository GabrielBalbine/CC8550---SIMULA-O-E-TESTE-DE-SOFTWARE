from locust import HttpUser, task, between

class UsuarioBlackFriday(HttpUser):
    host = "http://localhost:8000"

    wait_time = between(1, 3)

    @task
    def home(self):
        self.client.get("/")