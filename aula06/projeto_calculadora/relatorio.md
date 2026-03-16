# Relatório de Testes - Calculadora com Repositório

## 1. Resultados dos Testes
Todos os testes foram implementados e executados com sucesso utilizando a biblioteca `unittest`. A suíte foi dividida em três frentes:
* **Testes de Unidade:** Validaram isoladamente a lógica matemática, tipagem, limites e tratamento de exceções (divisão por zero, etc).
* **Testes de Integração:** Validaram a comunicação real entre a `Calculadora` e o `HistoricoRepositorio`, garantindo que o estado (histórico) é mantido sequencialmente.
* **Testes com Test Doubles:** Isolaram completamente a calculadora usando `MagicMock` para verificar tanto os retornos (Stubs) quanto as interações de salvamento (Mocks).

## 2. Bug Encontrado e Corrigido
Durante a implementação dos testes com Mock para a função `potencia`, identificamos um defeito intencional de formatação de string.
* **O defeito:** O método estava registrando a operação no repositório com o operador incorreto ou mal formatado na string de histórico.
* **A correção:** O código em `src/calculadora.py` foi ajustado para utilizar a string correta: `f"{base} ** {expoente} = {resultado}"`. O teste `test_mock_detecta_bug_potencia` utilizando Mock confirmou a chamada correta do método `salvar()`.

## 3. Cobertura Obtida
Utilizando a ferramenta `coverage.py`, obtivemos **97% de cobertura total** do projeto. 

```text
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/calculadora.py            43      2    95%   16, 42
src/repositorio.py            11      0   100%
tests/test_doubles.py         46      1    98%   73
tests/test_integracao.py      34      1    97%   52
tests/test_unidade.py         62      1    98%   92
--------------------------------------------------------
TOTAL                        196      5    97%