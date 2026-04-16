# Sistema Task Manager - CC8550

Repositório contendo o Sistema de Gerenciamento de Tarefas desenvolvido para a Atividade 09 da disciplina de Simulação e Teste de Software (CC8550). O objetivo é aplicar testes orientados a objetos e componentes, utilizando Mocks e Stubs.

## Estrutura do Projeto

\`\`\`text
task_manager/
  ├── __init__.py
  ├── task.py          # Entidade principal e regras de negócio
  ├── storage.py       # Banco de dados em memória (InMemoryStorage)
  ├── repository.py    # Repositório de tarefas
  └── service.py       # (Bônus) Camada de serviços
tests/
  ├── __init__.py
  ├── test_task.py       # Testes Unitários (Foco em Estado e Ciclo de vida)
  └── test_repository.py # Testes de Componente (Foco em Interação com Mocks/Stubs)
requirements.txt
README.md
\`\`\`

## Como Instalar

Certifique-se de ter o Python 3.8+ instalado. No terminal, na raiz do projeto, instale as dependências executando:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Como Testar

Para executar toda a suíte de testes (garantindo que Mocks, Stubs e Validações de Estado estão funcionando corretamente), rode o comando abaixo no terminal:

\`\`\`bash
pytest -v
\`\`\`

*(A flag `-v` serve para exibir o relatório detalhado com o nome de cada teste passando).*