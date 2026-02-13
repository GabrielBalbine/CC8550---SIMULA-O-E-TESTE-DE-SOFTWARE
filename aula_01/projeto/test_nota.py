import pytest
from sistema_notas import validar_nota

def test_validar_nota():
    assert validar_nota(0) is True
    assert validar_nota(5.5) is True
    assert validar_nota(10) is True

    assert validar_nota(-0.1) is False
    assert validar_nota(10.1) is False 
    assert validar_nota("banana") is False 

from sistema_notas import calcular_media

def test_calcular_media_simples():
    # caminho feliz: 3 notas válidas
    assert calcular_media([5, 7, 9]) == 7
    assert calcular_media([5, 5, 5]) == 5
    assert calcular_media([9, 9, 9]) == 9 

def test_calcular_media_ignora_invalidas():
    #se tudo correr certo, ignora o 50 e o -5, então calcula a média entre 8 e 10, que deve ser 9
    assert calcular_media([8, 10, 50, -5]) == 9

def test_calcular_media_erro_vazia():
    # teste se ele calcula uma média vazia, se tudo der certo, não
    with pytest.raises(ValueError):
        calcular_media([])

def test_calcular_media_erro_todas_invalidas():
    # se apenas tiverem formatos inválidos, ele reclama também
    with pytest.raises(ValueError):
        calcular_media([11, -1, "zero"])


from sistema_notas import obter_situacao

@pytest.mark.parametrize("media, esperado", [
    (10, "Aprovado"),
    (7.0, "Aprovado"),      # testando o limite exato da aprovação, limite da gameplay
    (6.9, "Recuperacao"),   # testando a falta de um pentelhésimo
    (5.0, "Recuperacao"),   # testando recuperação
    (4.9, "Reprovado"),     # testando a quase recuperação
    (0, "Reprovado"),
    (1, "Reprovado"),
    (2, "Reprovado"),
    (8, "Aprovado"),
    (10, "Aprovado"),
    (9.5, "Aprovado"),
    (4, "Reprovado"),
    (3, "Reprovado"),
    (4.8, "Reprovado")
])
def test_obter_situacao_parametrizado(media, esperado):
    assert obter_situacao(media) == esperado

def test_obter_situacao_erro():
    # prova de fogo, caso dê 11 por algum motivo
    with pytest.raises(ValueError):
        obter_situacao(11)

from sistema_notas import calcular_estatisticas

def test_calcular_estatisticas_aaa():
    # cria um caso de cada, pra garantir que tá boneco
    notas = [9.0, 7.0, 5.0, 3.0, 15.0]
    
    resultado = calcular_estatisticas(notas)
    
    # média: (9+7+5+3)/4 = 24/4 = 6.0
    assert resultado["media"] == 6.0
    assert resultado["maior"] == 9.0
    assert resultado["menor"] == 3.0
    assert resultado["aprovados"] == 2
    assert resultado["recuperacao"] == 1
    assert resultado["reprovados"] == 1

def test_estatisticas_lista_vazia():
    # lista vazia taca zero em tudo, pelo menos é pra ocorrer
    resultado = calcular_estatisticas([])
    assert resultado["media"] == 0.0
    assert resultado["aprovados"] == 0


from sistema_notas import normalizar_notas

def test_normalizar_base_20():

    notas = [20, 10, 0]
    esperado = [10.0, 5.0, 0.0]
    
    assert normalizar_notas(notas, nota_maxima=20) == esperado

def test_normalizar_base_100():

    #apenas pela ciencia
    assert normalizar_notas([75], nota_maxima=100) == [7.5]

def test_normalizar_valores_quebrados():
    # ver se funciona com dizima periodica
    
    resultado = normalizar_notas([10], nota_maxima=30)
    
    # usa a verificação de aproximação do pytest e coloca uma tolerância de 0.01
    assert resultado == pytest.approx([3.33], abs=0.01)