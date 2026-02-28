import pytest

def acesso(idade, membro):
    if idade >= 18 and membro:
        return "Permitido"
    return "Negado"

# Testando todas as 4 combinações da Cobertura de Condição
@pytest.mark.parametrize("idade, membro, esperado", [
    (20, True, "Permitido"), # V e V
    (20, False, "Negado"),   # V e F
    (15, True, "Negado"),    # F e V
    (15, False, "Negado")    # F e F
], ids=["VV_permitido", "VF_negado", "FV_negado", "FF_negado"])
def test_cobertura_condicao(idade, membro, esperado):
    assert acesso(idade, membro) == esperado