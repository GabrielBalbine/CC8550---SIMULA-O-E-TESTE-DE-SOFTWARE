import pytest

def percorrer_matriz(m, n):
    for i in range(m):
        for j in range(n):
            print(f"Posicao ({i}, {j})")

@pytest.mark.parametrize("m, n, qtd_prints_esperada", [
    (0, 0, 0), # 1. Ambos ignorados (0x0 = 0)
    (1, 0, 0), # 2. Apenas 'j' ignorado (1x0 = 0)
    (1, 3, 3), # 3. Um laço 1x, outro várias (1x3 = 3)
    (2, 2, 4)  # 4. Ambos várias vezes (2x2 = 4)
], ids=["ambos_ignorados", "j_ignorado", "um_vez_outro_varias", "ambos_varias"])
def test_percorrer_matriz(capsys, m, n, qtd_prints_esperada):
    # Act: Roda a função
    percorrer_matriz(m, n)
    
    # Captura tudo que foi printado no terminal
    captured = capsys.readouterr()
    
    # Assert: Conta quantas linhas foram geradas (cada print = 1 linha)
    linhas_printadas = len(captured.out.splitlines())
    
    assert linhas_printadas == qtd_prints_esperada