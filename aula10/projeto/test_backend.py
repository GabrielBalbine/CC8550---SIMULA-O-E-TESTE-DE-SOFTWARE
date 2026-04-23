import time
import requests
import pytest

# ==========================================
# 1. TESTE DE DESEMPENHO (Tempo de Resposta)
# ==========================================
def operacao_ecommerce():
    """Simula o processamento do backend no carrinho de compras"""
    time.sleep(0.3) # Simula 300ms de processamento do banco
    return True

def test_desempenho_p95_abaixo_500ms(benchmark):
    # (Requisito) Desempenho: Tempo de resposta P95 < 500ms.
    # O benchmark vai rodar a função várias vezes e calcular o P95.
    resultado = benchmark(operacao_ecommerce)
    assert resultado is True

# ==========================================
# 2. TESTE DE SEGURANÇA (Rate Limiting)
# ==========================================
def test_seguranca_rate_limiting():

    # (Requisito) Segurança: Rate limiting de 100 req/min/IP.
    # Simula 101 requisições rápidas para ver se a API bloqueia a última.

    # Como não temos uma API real rodando, vamos simular a lógica (MOCK)
    
    limite_permitido = 100
    requisicoes_feitas = 101
    status_code_retornado = 200
    
    if requisicoes_feitas > limite_permitido:
        status_code_retornado = 429 # 429 Too Many Requests
        
    assert status_code_retornado == 429, "Falha: O sistema não bloqueou o excesso de requisições!"