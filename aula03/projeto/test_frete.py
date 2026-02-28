import pytest
from frete import calcular_frete
from hypothesis import given, strategies as st

# 1 - Classes de Equivalência (5 casinhos)
@pytest.mark.parametrize("peso, destino, valor_pedido, esperado", [
    # 1. Até 1kg, mesma região
    (0.5, "mesma região", 100.0, 10.0),
    
    # 2. De 1 a 5kg, outra região
    (3.0, "outra região", 100.0, 22.5),
    
    # 3. De 5 a 20kg, internacional
    (10.0, "internacional", 100.0, 50.0),
    
    # 4. Frete Grátis (Valor > 200( peso e destino deixam de importar)
    (15.0, "mesma região", 250.0, 0.0),
    
    # 5. Extra - Até 1kg, internacional
    (0.8, "internacional", 50.0, 20.0)],

    ids=["peso_baixo_regiao", "peso_medio_outra", "peso_alto_inter", "frete_gratis", "peso_baixo_inter"])
def test_classes_equivalencia_validas(peso, destino, valor_pedido, esperado):
    # Act & Assert
    assert calcular_frete(peso, destino, valor_pedido) == esperado


# ==========================================
# Entradas inválidas
@pytest.mark.parametrize("peso, destino, valor_pedido, mensagem_erro", [
    #1: Peso Zero/Negativo
    (0.0, "mesma região", 100.0, "zero ou negativo"),
    
    #2: Peso acima de 20kg
    (25.0, "mesma região", 100.0, "acima de 20 kg"),
    
    #3: Destino que não existe
    (2.0, "narnia", 100.0, "Destino inválido")], 
    ids=["erro_peso_zero", "erro_peso_gigante", "erro_destino_falso"])
def test_entradas_invalidas(peso, destino, valor_pedido, mensagem_erro):
    # Act & Assert
    with pytest.raises(ValueError) as erro_info:
        calcular_frete(peso, destino, valor_pedido)
        
    # verifica o erro com oq tem no código 
    assert mensagem_erro in str(erro_info.value)


# valores limite
@pytest.mark.parametrize("peso, esperado", [
    # --- Fronteira 1: 1 kg ---
    (0.9, 10.0),  
    (1.0, 10.0),  
    (1.1, 15.0),  

    # --- Fronteira 2: 5 kg ---
    (4.9, 15.0),  
    (5.0, 15.0),  
    (5.1, 25.0),  

    # --- Fronteira 3: 20 kg ---
    (19.9, 25.0), 
    (20.0, 25.0), 
    (20.1, "erro") ],
    ids=[
    "f1_antes", "f1_exato", "f1_depois",
    "f2_antes", "f2_exato", "f2_depois",
    "f3_antes", "f3_exato", "f3_depois"])


def test_valores_limite_peso(peso, esperado):
    destino_fixo = "mesma região"
    pedido_fixo = 100.0
    
    if esperado == "erro":
        with pytest.raises(ValueError) as erro_info:
            calcular_frete(peso, destino_fixo, pedido_fixo)
        assert "acima de 20 kg" in str(erro_info.value)
    
    else:
        assert calcular_frete(peso, destino_fixo, pedido_fixo) == esperado

# ==========================================
# Hypothesis

st_peso_valido = st.floats(min_value=0.1, max_value=20.0) # Gera pesos de 0.1 a 20.0
st_destino_valido = st.sampled_from(["mesma região", "outra região", "internacional"]) # Sorteia um dos 3
st_valor_qualquer = st.floats(min_value=0.0, max_value=5000.0) # Gera valores de 0 a 5000

# ---------------------------------------------------------
# 1: Frete nunca é negativo
# ---------------------------------------------------------
@given(peso=st_peso_valido, destino=st_destino_valido, valor_pedido=st_valor_qualquer)
def test_frete_nunca_negativo(peso, destino, valor_pedido):
    resultado = calcular_frete(peso, destino, valor_pedido)
    assert resultado >= 0.0

# ---------------------------------------------------------
# 2: Pedido acima de R$ 200,00 sempre retorna 0,0
# ---------------------------------------------------------
@given(peso=st_peso_valido, destino=st_destino_valido, valor_pedido=st.floats(min_value=200.01, max_value=10000.0))
def test_frete_gratis_acima_200(peso, destino, valor_pedido):
    resultado = calcular_frete(peso, destino, valor_pedido)
    assert resultado == 0.0

# ---------------------------------------------------------
# 3: Frete "outra região" > frete "mesma região"
# ---------------------------------------------------------
# PULO DO GATO: O valor do pedido AQUI tem que ser menor ou igual a 200.
# Se for maior que 200, o frete zera pra todo mundo, e 0.0 NÃO É maior que 0.0 (o teste falharia à toa!)
@given(peso=st_peso_valido, valor_pedido=st.floats(min_value=0.0, max_value=200.0))
def test_outra_regiao_mais_cara(peso, valor_pedido):
    frete_mesma = calcular_frete(peso, "mesma região", valor_pedido)
    frete_outra = calcular_frete(peso, "outra região", valor_pedido)
    
    assert frete_outra > frete_mesma