import unittest
import sys
import os

# Ajuste no path para importar da pasta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculadora import Calculadora
from src.repositorio import HistoricoRepositorio

class TestIntegracao(unittest.TestCase):
    def setUp(self):
        # Repositório REAL sendo instanciado
        self.repo = HistoricoRepositorio()
        self.calc = Calculadora(self.repo)

    # --- 3.1 Operações Sequenciais ---
    def test_operacoes_sequenciais(self):
        # 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        self.calc.somar(2, 3)
        self.calc.multiplicar(self.calc.obter_ultimo_resultado(), 4)
        self.calc.dividir(self.calc.obter_ultimo_resultado(), 2)

        self.assertEqual(self.calc.obter_ultimo_resultado(), 10)
        self.assertEqual(self.repo.total(), 3)

    # --- 3.2 Consistência do Histórico ---
    def test_historico_registra_formato_correto(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(4, 5)
        registros = self.repo.listar()
        
        # O assert verifica se a formatação bate EXATAMENTE com a string do código
        self.assertIn("2 + 3 = 5", registros)
        self.assertIn("4 * 5 = 20", registros)

    def test_limpar_historico(self):
        self.calc.somar(1, 1)
        self.repo.limpar()
        self.assertEqual(self.repo.total(), 0)

    def test_historico_com_excecao_nao_registra_falhas(self):
        # Se uma operação falhar (ex: divisão por zero), ela NÃO deve ir pro histórico
        self.calc.somar(10, 5) # Dá 15 (vai pro histórico)
        
        with self.assertRaises(ValueError):
            self.calc.dividir(15, 0) # Falha (NÃO deve ir pro histórico)
            
        self.assertEqual(self.repo.total(), 1)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 15)

if __name__ == '__main__':
    unittest.main()