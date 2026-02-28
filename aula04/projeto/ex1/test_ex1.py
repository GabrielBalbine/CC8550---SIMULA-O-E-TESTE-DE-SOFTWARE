import pytest

# Trazendo a função pro arquivo de teste
def verificar(n):
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"

@pytest.mark.parametrize("n_entrada, esperado", [
    (2, "Par positivo"),    # Cobre o Caminho 1 (Maior que zero e par)
    (3, "Impar positivo"),  # Cobre o Caminho 2 (Maior que zero e impar)
    (-5, "Negativo"),       # Cobre o Caminho 3 (Menor que zero)
    (0, "Zero")             # Cobre o Caminho 4 (Falha em tudo e cai no else final)
], ids=["caminho1_par_pos", "caminho2_impar_pos", "caminho3_negativo", "caminho4_zero"])
def test_verificar_caminhos_independentes(n_entrada, esperado):
    # Act & Assert
    assert verificar(n_entrada) == esperado