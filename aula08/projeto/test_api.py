import requests
import pytest
import jsonschema

# URLs base para os testes
BASE_URL = "https://jsonplaceholder.typicode.com"
REQRES_URL = "https://reqres.in/api"
HTTPBIN_URL = "https://httpbin.org"

# Schema esperado para um "Post" do JSONPlaceholder
SCHEMA_POST = {
    "type": "object",
    "required": ["id", "title", "body", "userId"],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"}
    }
}

@pytest.fixture
def post_criado():
    """
    (Requisito 9) Fixture que cria um recurso antes do teste e remove após.
    Retorna os dados do post criado.
    """
    payload = {"title": "Post Temporário", "body": "Conteúdo", "userId": 1}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    post = resp.json()
    
    yield post
    
    # Teardown: Simula a exclusão do recurso
    requests.delete(f"{BASE_URL}/posts/{post['id']}")

def test_get_colecao():
    """
    (Requisito 1) GET em coleção - status 200, lista não vazia.
    """
    resp = requests.get(f"{BASE_URL}/posts")
    assert resp.status_code == 200
    assert len(resp.json()) > 0

def test_get_recurso_schema():
    """
    (Requisito 2) GET em recurso existente - validar schema com jsonschema.
    """
    resp = requests.get(f"{BASE_URL}/posts/1")
    assert resp.status_code == 200
    jsonschema.validate(instance=resp.json(), schema=SCHEMA_POST)

def test_get_recurso_inexistente():
    """
    (Requisito 3) GET em recurso inexistente - status 404.
    """
    resp = requests.get(f"{BASE_URL}/posts/999999")
    assert resp.status_code == 404

def test_post_criar_recurso():
    """
    (Requisito 4) POST criando recurso - status 201, id no retorno.
    """
    payload = {"title": "Novo Teste", "body": "Testando API", "userId": 1}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    
    data = resp.json()
    assert "id" in data
    assert data["title"] == payload["title"]

def test_patch_atualizar_recurso():
    """
    (Requisito 5) PUT ou PATCH atualizando recurso - campo alterado.
    """
    payload = {"title": "Titulo Atualizado"}
    resp = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert resp.status_code == 200
    
    data = resp.json()
    assert data["title"] == "Titulo Atualizado"

def test_delete_recurso():
    """
    (Requisito 6) DELETE - status 200 ou 204.
    JSONPlaceholder retorna 200 para operações DELETE bem-sucedidas.
    """
    resp = requests.delete(f"{BASE_URL}/posts/1")
    assert resp.status_code == 200

def test_post_dados_invalidos():
    """
    (Requisito 7) Envio de dados inválidos - status 4xx.
    Testa a API ReqRes tentando registrar um usuário sem senha (gera Bad Request ou Unauthorized).
    """
    payload_invalido = {"email": "sydney@fife"} # Faltando o password
    resp = requests.post(f"{REQRES_URL}/register", json=payload_invalido)
    assert 400 <= resp.status_code < 500

def test_endpoint_autenticado():
    """
    (Requisito 8) Endpoint autenticado: com e sem credencial.
    Testa a API HttpBin que exige Authorization Bearer token.
    """
    url_auth = f"{HTTPBIN_URL}/bearer"
    
    # Sem credencial -> 401 Unauthorized
    resp_sem_token = requests.get(url_auth)
    assert resp_sem_token.status_code == 401
    
    # Com credencial -> 200 OK
    headers = {"Authorization": "Bearer meu_token_secreto_123"}
    resp_com_token = requests.get(url_auth, headers=headers)
    assert resp_com_token.status_code == 200
    assert resp_com_token.json()["authenticated"] is True

def test_usar_fixture(post_criado):
    """
    (Requisito 9.2) Teste que consome a fixture criada.
    Garante que o post criado no setup tem os dados corretos.
    """
    assert "id" in post_criado
    assert post_criado["title"] == "Post Temporário"

def test_performance_tempo_resposta():
    """
    (Requisito 10) Asserção de tempo de resposta < 2,0 s.
    """
    resp = requests.get(f"{BASE_URL}/posts")
    tempo_segundos = resp.elapsed.total_seconds()
    assert tempo_segundos < 2.0