import pytest
from sistema import calcular_total, tem_estoque, aplicar_desconto, frete_gratis, calcular_lucro

# 1. Testes para calcular_total (Gera 4 testes)
@pytest.mark.parametrize("preco, quantidade, esperado", [
    (50, 2, 100),       # Compra normal
    (0, 5, 0),          # Item dado de graça em evento
    (100, 0, 0),        # Quantidade zero (cliente desistiu)
    (25.5, 2, 51.0)     # Valor quebrado
])
def test_calcular_total(preco, quantidade, esperado):
    assert calcular_total(preco, quantidade) == esperado

# 2. Testes para tem_estoque (Gera 4 testes)
@pytest.mark.parametrize("estoque, desejada, esperado", [
    (10, 5, True),      # Tem sobra no baú
    (10, 10, True),     # Limite exato (Sniper de mutante)
    (10, 15, False),    # Faltando estoque
    (0, 1, False)       # Estoque zerado
])
def test_tem_estoque(estoque, desejada, esperado):
    assert tem_estoque(estoque, desejada) is esperado

# 3. Testes para aplicar_desconto (Gera 4 testes)
@pytest.mark.parametrize("valor, cupom, esperado", [
    (100, "PHOBIA_VIP", 80.0),  # Cupom válido
    (100, "FALSO", 100.0),      # Cupom incorreto
    (100, "", 100.0),           # Sem cupom nenhum
    (100, "phobia_vip", 100.0)  # Letra minúscula (tem que recusar)
])
def test_aplicar_desconto(valor, cupom, esperado):
    assert aplicar_desconto(valor, cupom) == esperado

# 4. Testes para frete_gratis (Gera 4 testes)
@pytest.mark.parametrize("valor, esperado", [
    (1500, True),       # Bem acima do limite
    (1001, True),       # Um real acima (Sniper)
    (1000, False),      # Exatamente no limite (Sniper de mutante)
    (500, False)        # Abaixo do limite
])
def test_frete_gratis(valor, esperado):
    assert frete_gratis(valor) is esperado

# 5. Testes para calcular_lucro (Gera 4 testes)
@pytest.mark.parametrize("venda, custo, esperado", [
    (200, 50, 150),     # Lucro limpo
    (100, 100, 0),      # Empate (Zero a zero)
    (50, 100, -50),     # Prejuízo (Roupa encalhada)
    (0, 50, -50)        # Só custo de fabricação, nenhuma venda
])
def test_calcular_lucro(venda, custo, esperado):
    assert calcular_lucro(venda, custo) == esperado