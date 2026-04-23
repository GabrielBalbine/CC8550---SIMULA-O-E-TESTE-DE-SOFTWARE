from locust import HttpUser, task, between

class UsuarioBlackFriday(HttpUser):
    wait_time = between(1, 3)

    @task(3) 
    def navegar_produtos(self):
        pass

    @task(1)
    def finalizar_compra(self):
        pass


# Para Teste de Carga (> 2000 req/s):
# Comando: locust -f locustfile.py --users 10000 --spawn-rate 100
# Para Teste de Estresse (Achar ponto de quebra > 15.000 usuários):
# Comando: locust -f locustfile.py --users 20000 --spawn-rate 500 