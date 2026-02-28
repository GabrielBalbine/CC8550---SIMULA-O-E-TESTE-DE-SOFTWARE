import pytest

def somar_ate(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma

@pytest.mark.parametrize("n_entrada, esperado", [
    (0, 0), # Laço ignorado (0 iterações)
    (1, 0), # Laço executado 1 vez (i=0)
    (3, 3)  # Laço executado várias vezes (i=0, 1 e 2. Soma = 3)
], ids=["zero_iteracoes", "uma_iteracao", "varias_iteracoes"])
def test_teste_de_ciclo(n_entrada, esperado):
    assert somar_ate(n_entrada) == esperado