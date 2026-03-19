import unittest
from unittest.mock import MagicMock
import sys
import os

# Ajuste no path para importar da pasta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculadora import Calculadora

class TestUnidadeCalculadora(unittest.TestCase):
    def setUp(self):
        # Stub: imita o repositorio para isolar a calculadora
        self.repo = MagicMock() 
        self.calc = Calculadora(self.repo)

    # --- 2.1 Testes de Entrada e Saída ---
    def test_soma_retorna_valor_correto(self):
        self.assertEqual(self.calc.somar(5, 3), 8)
        self.assertEqual(self.calc.somar(-2, 2), 0)

    def test_subtracao_retorna_valor_correto(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)
        self.assertEqual(self.calc.subtrair(0, 5), -5)

    def test_multiplicacao_retorna_valor_correto(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 6)
        self.assertEqual(self.calc.multiplicar(-2, 4), -8)

    def test_divisao_retorna_valor_correto(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)
        self.assertEqual(self.calc.dividir(9, 3), 3.0)

    def test_potencia_retorna_valor_correto(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)

    def test_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    # --- 2.2 Testes de Tipagem ---
    def test_tipagem_string_rejeitada(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_tipagem_none_rejeitado(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)

    def test_tipagem_bool_aceito(self):
        # Em Python, bool herda de int (True=1, False=0). 
        # O comportamento esperado é não dar erro!
        self.assertEqual(self.calc.somar(True, False), 1)

    # --- 2.3 Testes de Limite Inferior e Superior ---
    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_limite_float_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_float_grande(self):
        grande = sys.float_info.max / 2
        resultado = self.calc.somar(grande, grande)
        self.assertFalse(resultado == float('inf'))

    def test_limite_divisor_muito_pequeno(self):
        self.assertAlmostEqual(self.calc.dividir(1, 1e-10), 1e10)

    def test_limite_expoente_negativo_e_fracionario(self):
        self.assertEqual(self.calc.potencia(2, -1), 0.5)
        self.assertEqual(self.calc.potencia(4, 0.5), 2.0)

    # --- 2.4 e 2.5 Testes de Exceção e Mensagens de Erro ---
    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.multiplicar("x", 1)

    # --- 2.6 Testes de Fluxos de Controle ---
    def test_caminho_divisao_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_caminho_divisao_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()