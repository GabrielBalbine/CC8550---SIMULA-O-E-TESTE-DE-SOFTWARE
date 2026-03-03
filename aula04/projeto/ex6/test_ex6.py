import pytest

def analisar(numeros):
    total = 0
    for n in numeros:
        if n > 0 and n % 2 == 0:
            total += n
        elif n < 0:
            total -= 1
        else:
            continue
    if total > 10:
        return "Acima"
    return "Abaixo"

@pytest.mark.parametrize("lista, esperado", [
    # Cobertura de Comandos (C0), Ramos (C1) e Laço (várias iterações)
    ([12, -1, 3], "Acima"),  
    
    # Cobertura de Laço: 0 iterações (lista vazia)
    ([], "Abaixo"),          
    
    # Cobertura de Laço: 1 iteração
    ([2], "Abaixo"),         
    
    # Cobertura de Condição (n > 0 and n % 2 == 0)
    # V e V (já coberto pelo 12 e pelo 2 acima, mas vamos isolar um)
    ([4], "Abaixo"),
    # V e F (n=3, cai no continue)
    ([3], "Abaixo"),
    # F e F/V (n=-2, curto-circuito no n>0, cai no elif)
    ([-2], "Abaixo")         
])
def test_analisar_integrador(lista, esperado):
    assert analisar(lista) == esperado