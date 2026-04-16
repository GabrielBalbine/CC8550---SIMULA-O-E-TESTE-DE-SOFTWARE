import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)

# 1. Estado inicial (Teste de estado)
def test_estado_inicial(task_valida):
    task_valida.validar() # não deve lançar erro
    assert task_valida.titulo == "Estudar"
    assert task_valida.status == Status.PENDENTE # estado padrão

# 2. Validação: Título inválido
def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError, match="3 caracteres"):
        task.validar()

# 3. Validação: Prazo no passado
def test_prazo_no_passado_invalido():
    prazo = datetime.now() - timedelta(days=1) # Prazo de ontem
    task = Task(None, "Fazer TCC", "Documentação", Priority.ALTA, prazo)
    with pytest.raises(ValueError, match="no passado"):
        task.validar()

# 4. Ciclo de vida: Transição válida
def test_ciclo_vida_transicao(task_valida):
    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO # estado mudou

# 5. Ciclo de vida: Transição inválida
def test_ciclo_vida_transicao_invalida(task_valida):
    # Tentar definir um status com um valor fora do enum deve lançar ValueError
    with pytest.raises(ValueError):
        task_valida.status = "FINALIZADO"