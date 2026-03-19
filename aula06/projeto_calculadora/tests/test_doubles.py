import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculadora import Calculadora

class TestComStub(unittest.TestCase):
    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        # A calculadora pode ser testada mesmo antes do repositorio existir
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)
        
    # --- Teste Extra de Stub ---
    def test_stub_simula_repositorio_cheio(self):
        # Forçamos o stub a mentir que tem 100 itens pra ver se o código aceita
        self.stub_repo.total.return_value = 100
        self.assertEqual(self.stub_repo.total(), 100)


class TestComMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        # Verifica que salvar() foi chamado exatamente uma vez
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto(self):
        self.calc.somar(4, 6)
        # Verifica o argumento exato passado ao repositorio
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_nao_chamado_em_excecao(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)
        # Se houve excecao, o repositorio NAO deve ter sido acionado
        self.mock_repo.salvar.assert_not_called()

    # --- Tarefa 1: Verificar argumento passado a salvar() para todas as operações ---
    def test_mock_argumento_correto_todas_operacoes(self):
        self.calc.subtrair(10, 5)
        self.mock_repo.salvar.assert_called_with("10 - 5 = 5")
        
        self.calc.multiplicar(2, 3)
        self.mock_repo.salvar.assert_called_with("2 * 3 = 6")
        
        self.calc.dividir(10, 2)
        self.mock_repo.salvar.assert_called_with("10 / 2 = 5.0")

    # --- Tarefa 2 e 3: Detectar e validar a correção do bug em potencia ---
    def test_mock_detecta_bug_potencia(self):
        self.calc.potencia(2, 3)
        # Como já corrigi o código no começo (trocando pra **), esse teste vai PASSAR!
        self.mock_repo.salvar.assert_called_with("2 ** 3 = 8")

if __name__ == '__main__':
    unittest.main()