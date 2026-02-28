import pytest

def classificar(x):
    if x > 100:
        return "Alto"
    if x > 50:
        return "Medio"
    return "Baixo"

# Os 3 CTs cobrem 100% de C0 (Comandos) e 100% de C1 (Ramos)
@pytest.mark.parametrize("x_entrada, esperado", [
    (150, "Alto"),   # Cobre: if > 100 (Sim) e linha do return Alto
    (75, "Medio"),   # Cobre: if > 100 (Não), if > 50 (Sim) e linha do return Medio
    (30, "Baixo")    # Cobre: if > 50 (Não) e linha do return Baixo
], ids=["ct1_alto", "ct2_medio", "ct3_baixo"])
def test_cobertura_comandos_e_ramos(x_entrada, esperado):
    assert classificar(x_entrada) == esperado