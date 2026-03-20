import unittest
from estoque import Estoque

class TestEstoque(unittest.TestCase):
    def setUp(self):
        self.estoque = Estoque()

    # --- adicionar_produto e consultar_quantidade ---
    
    # RED: Criar teste para adicionar e consultar um item novo
    # GREEN: Usar um dicionário simples
    # REFACTOR: Adicionar tipagem no código fonte
    def test_adicionar_novo_produto_deve_constar_no_estoque(self):
        self.estoque.adicionar_produto("Camiseta", 10)
        self.assertEqual(self.estoque.consultar_quantidade("Camiseta"), 10)

    # RED: Teste falha porque o dicionário substituía o valor
    # GREEN: Atualizar adicionar_produto para somar com o estoque atual
    def test_adicionar_produto_existente_deve_somar_quantidades(self):
        self.estoque.adicionar_produto("Tenis", 5)
        self.estoque.adicionar_produto("Tenis", 3)
        self.assertEqual(self.estoque.consultar_quantidade("Tenis"), 8)

    # RED: Teste para barrar adição <= 0
    # GREEN: Adicionar IF levantando ValueError
    def test_adicionar_quantidade_invalida_deve_levantar_excecao(self):
        with self.assertRaises(ValueError):
            self.estoque.adicionar_produto("Meia", 0)
        with self.assertRaises(ValueError):
            self.estoque.adicionar_produto("Meia", -5)

    # RED: Testar produto que não existe
    # GREEN: Usar dict.get(nome, 0)
    def test_consultar_produto_inexistente_deve_retornar_zero(self):
        self.assertEqual(self.estoque.consultar_quantidade("Fantasma"), 0)


    # --- remover_produto ---

    # RED: Teste para subtrair itens
    # GREEN: Fazer a subtração simples no dicionário
    def test_remover_produto_deve_diminuir_estoque(self):
        self.estoque.adicionar_produto("Bermuda", 20)
        self.estoque.remover_produto("Bermuda", 5)
        self.assertEqual(self.estoque.consultar_quantidade("Bermuda"), 15)

    # RED: Teste de saque a descoberto
    # GREEN: Adicionar IF consultando estoque atual antes de remover
    def test_remover_mais_que_disponivel_deve_levantar_excecao(self):
        self.estoque.adicionar_produto("Bone", 5)
        with self.assertRaises(ValueError):
            self.estoque.remover_produto("Bone", 10)

    # RED: Teste para barrar remoção <= 0
    # GREEN: Adicionar IF inicial na função remover
    def test_remover_quantidade_invalida_deve_levantar_excecao(self):
        self.estoque.adicionar_produto("Cinto", 10)
        with self.assertRaises(ValueError):
            self.estoque.remover_produto("Cinto", -2)


    # --- listar_produtos ---

    # RED: Teste para listar zerados
    # GREEN: Fazer list comprehension filtrando itens com valor 0
    def test_listar_produtos_deve_retornar_apenas_zerados(self):
        self.estoque.adicionar_produto("Mochila", 10)
        self.estoque.adicionar_produto("Carteira", 5)
        self.estoque.remover_produto("Carteira", 5) # Zerou a carteira
        
        zerados = self.estoque.listar_produtos()
        self.assertIn("Carteira", zerados)
        self.assertNotIn("Mochila", zerados)


    # --- produto_mais_estocado ---

    # RED: Teste para buscar o campeão de vendas
    # GREEN: Usar a função max() do Python
    def test_produto_mais_estocado_retorna_o_maior(self):
        self.estoque.adicionar_produto("A", 10)
        self.estoque.adicionar_produto("B", 50)
        self.estoque.adicionar_produto("C", 30)
        self.assertEqual(self.estoque.produto_mais_estocado(), "B")

    # RED: Testar busca em estoque vazio
    # GREEN: Retornar None se dict estiver vazio
    def test_produto_mais_estocado_vazio_deve_retornar_none(self):
        self.assertIsNone(self.estoque.produto_mais_estocado())

if __name__ == '__main__':
    unittest.main()