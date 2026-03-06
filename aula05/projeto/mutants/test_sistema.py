# arquivo: test_sistema.py
import pytest
from sistema import calcular_total, tem_estoque, aplicar_desconto, frete_gratis, calcular_lucro

def test_calcular_total():
    assert calcular_total(50, 2) == 100

def test_tem_estoque():
    assert tem_estoque(10, 5) is True
    # O teste abaixo é o tiro de sniper que mata o Mutante 2:
    assert tem_estoque(10, 10) is True 
    assert tem_estoque(10, 15) is False

def test_aplicar_desconto():
    assert aplicar_desconto(100, "PHOBIA_VIP") == 80.0
    # O teste abaixo mata o Mutante 3 garantindo que cupom errado não dá desconto:
    assert aplicar_desconto(100, "FALSO") == 100.0 

def test_frete_gratis():
    assert frete_gratis(1001) is True
    # O teste abaixo mata o Mutante 4 garantindo que exatos 1000 reais paga frete:
    assert frete_gratis(1000) is False 

def test_calcular_lucro():
    assert calcular_lucro(200, 50) == 150