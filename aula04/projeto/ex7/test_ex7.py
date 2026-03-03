import pytest
from ex7 import desconto

@pytest.mark.parametrize("preco, vip, esperado", [
    (100, False, 100), # Total > 50, Não VIP
    (40, False, 50),   # Total < 50, Não VIP
    (100, True, 80),   # Total > 50, É VIP
    (40, True, 50)     # Total < 50, É VIP
])
def test_desconto_all_uses(preco, vip, esperado):
    assert desconto(preco, vip) == esperado