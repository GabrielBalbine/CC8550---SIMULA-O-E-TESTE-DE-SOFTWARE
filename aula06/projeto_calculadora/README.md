# Projeto Calculadora - Testes de Unidade e Integração

Atividade 06 da disciplina de Simulação e Teste de Software.

## Como rodar o projeto

1. Instale as dependências:
`pip install -r requirements.txt`

2. Para rodar todos os testes:
`python -m unittest discover tests -v`

3. Para medir a cobertura:
`coverage run -m unittest discover tests`
`coverage report -m`