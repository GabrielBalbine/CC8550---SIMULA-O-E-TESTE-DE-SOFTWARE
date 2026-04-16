import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository

# Fixtures exigidas pelo professor
@pytest.fixture
def mock_storage():
    return Mock()

@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)

@pytest.fixture
def task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Fazer TCC", "Documentação", Priority.ALTA, prazo)

# 1. Teste de Interação e Estado: save() atribui ID
def test_save_atribui_id(repo, task):
    resultado = repo.save(task)
    assert resultado.id == 1

# 2. Teste de Mock (Verifica Comportamento): save() chama storage.add()
def test_save_chama_storage_add(repo, task, mock_storage):
    repo.save(task)
    # Verifica se o mock foi chamado com os argumentos certos
    mock_storage.add.assert_called_once_with(1, task)

# 3. Teste de Stub (Controla Estado): find_by_id() delega ao storage
def test_find_by_id_usa_storage(repo, task, mock_storage):
    # Stub: "Mente" que o storage.get retornou a nossa task
    mock_storage.get.return_value = task 
    
    resultado = repo.find_by_id(1)
    assert resultado == task

# 4. Sequência: save() seguido de find_by_id()
def test_save_seguido_de_find_by_id(repo, task, mock_storage):
    # Salva a task
    repo.save(task)
    
    # Prepara o stub pra devolver a task salva
    mock_storage.get.return_value = task
    
    encontrada = repo.find_by_id(1)
    assert encontrada.id == 1
    assert encontrada.titulo == "Fazer TCC"

# 5. Isolamento: find_all() retorna lista vazia quando não tem itens
def test_find_all_retorna_lista_vazia(repo, mock_storage):
    # Stub: Configura o mock pra devolver uma lista vazia
    mock_storage.get_all.return_value = []
    
    resultados = repo.find_all()
    assert resultados == []
    mock_storage.get_all.assert_called_once()