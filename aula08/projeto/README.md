# Suíte de Testes API REST - Simulação e Teste de Software

Repositório contendo a suíte de testes automatizados para APIs REST públicas, desenvolvido para a Atividade 08 da disciplina de Simulação e Teste de Software (CC8550).

## 1. APIs Escolhidas e Documentações
Para cobrir todos os cenários exigidos de forma eficiente, o projeto consome três APIs públicas e documentadas:
* **[JSONPlaceholder](https://jsonplaceholder.typicode.com/):** Usada para validação de fluxos CRUD, Schema e Performance.
* **[ReqRes](https://reqres.in/):** Usada para validar o tratamento de requisições com dados inválidos (Bad Request).
* **[HttpBin](https://httpbin.org/):** Usada para validar fluxos de Autenticação (Bearer Token).

## 2. Justificativa da Escolha
A integração destas três APIs permite testar 100% dos cenários exigidos na atividade sem a necessidade de criar contas ou gerenciar dados sensíveis localmente. O JSONPlaceholder oferece uma estrutura CRUD previsível, o ReqRes tem respostas úteis para validação de erros (`400 Bad Request`), e o HttpBin fornece endpoints para simulação de `401 Unauthorized` e sucesso na autenticação.

## 3. Instruções de Instalação
Certifique-se de ter o Python instalado. Clone este repositório e instale as dependências executando o comando abaixo no terminal da raiz do projeto:

```bash
pip install -r requirements.txt