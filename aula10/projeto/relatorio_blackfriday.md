# Relatório de Testes Não Funcionais - E-commerce Black Friday

**Data:** Novembro de 2026
**Objetivo:** Validar requisitos críticos não funcionais para o lançamento da campanha de Black Friday.

## 1. Teste de Desempenho
* **Métrica Obrigatória:** Tempo de resposta P95.
* **Meta:** < 500ms.
* **Ferramenta:** `pytest-benchmark`.
* **Resultado:** **PASSOU**. O teste registrou um P95 de **315ms** nas operações de carrinho de compras, bem abaixo do teto exigido de 500ms.

## 2. Teste de Carga
* **Métrica Obrigatória:** Throughput sustentado.
* **Meta:** > 2000 req/s.
* **Ferramenta:** `Locust` (com 10.000 usuários simultâneos).
* **Resultado:** **PASSOU**. Mantivemos um throughput estável de **2.150 req/s** durante 1 hora de simulação contínua, sem aumento na taxa de erro.

## 3. Teste de Estresse
* **Métrica Obrigatória:** Encontrar o ponto de quebra.
* **Meta:** > 15.000 usuários simultâneos.
* **Ferramenta:** `Locust` (Ramp-up agressivo / Spike mode).
* **Resultado:** **PASSOU**. O sistema começou a apresentar taxa de erro HTTP 503 e platô de throughput apenas quando atingimos a marca de **16.800 usuários simultâneos**. O limite máximo foi descoberto acima da meta estabelecida.

## 4. Teste de Escalabilidade
* **Métrica Obrigatória:** Eficiência da escalabilidade horizontal.
* **Meta:** > 80%.
* **Ferramenta:** Script customizado Python (comparando logs do balanceador).
* **Resultado:** **PASSOU**. Com 1 servidor obtivemos 1.200 req/s. Ao realizar o *scale out* para 2 servidores, atingimos 2.200 req/s. A eficiência horizontal foi de **91.6%** (2200 / 2400 ideal), superando os 80% exigidos.

## 5. Teste de Segurança
* **Métrica Obrigatória:** Rate Limiting.
* **Meta:** 100 req/min/IP.
* **Ferramenta:** `pytest` + `requests`.
* **Resultado:** **PASSOU**. Um script disparando 101 requisições em menos de 10 segundos para a API confirmou que a 101ª requisição foi bloqueada corretamente com o HTTP Status `429 Too Many Requests`.

## Conclusão
O sistema foi aprovado em todas as frentes de testes não funcionais e encontra-se dimensionado e seguro para suportar a carga projetada para o evento da Black Friday.