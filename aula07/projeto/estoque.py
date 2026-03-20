class Estoque:
    def __init__(self):
        self._produtos = {}

    def adicionar_produto(self, nome: str, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade a adicionar deve ser maior que zero")
        
        # Se o produto já existe, ele soma com o atual (get retorna 0 se não existir)
        estoque_atual = self._produtos.get(nome, 0)
        self._produtos[nome] = estoque_atual + quantidade

    def consultar_quantidade(self, nome: str) -> int:
        return self._produtos.get(nome, 0)

    def remover_produto(self, nome: str, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade a remover deve ser maior que zero")
        
        disponivel = self.consultar_quantidade(nome)
        if quantidade > disponivel:
            raise ValueError("Quantidade a remover é maior do que o estoque disponível")
        
        self._produtos[nome] -= quantidade

    def listar_produtos(self) -> list:
        # Retorna apenas os produtos cuja quantidade chegou a zero
        return [nome for nome, qtd in self._produtos.items() if qtd == 0]

    def produto_mais_estocado(self):
        if not self._produtos:
            return None
        # Retorna a chave (nome) que tem o maior valor (quantidade)
        return max(self._produtos, key=self._produtos.get)