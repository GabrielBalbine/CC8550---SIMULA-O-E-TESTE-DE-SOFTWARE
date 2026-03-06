
def calcular_total(preco, quantidade):
    return preco * quantidade

def tem_estoque(estoque_atual, quantidade_desejada):
    return estoque_atual >= quantidade_desejada

def aplicar_desconto(valor, cupom):
    if cupom == "PHOBIA_VIP":
        return valor * 0.8  # 20% de desconto
    return valor

def frete_gratis(valor_compra):
    return valor_compra > 1000

def calcular_lucro(venda, custo):
    return venda - custo