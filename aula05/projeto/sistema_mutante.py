def calcular_total(preco, quantidade):
    return preco / quantidade  # MUTANTE 1: Trocou multiplicação por divisão

def tem_estoque(estoque_atual, quantidade_desejada):
    return estoque_atual > quantidade_desejada  # MUTANTE 2: Tirou o "igual" do maior ou igual

def aplicar_desconto(valor, cupom):
    if cupom != "PHOBIA_VIP":  # MUTANTE 3: Trocou "==" por "!="
        return valor * 0.8
    return valor

def frete_gratis(valor_compra):
    return valor_compra >= 1000  # MUTANTE 4: Adicionou o "igual" no maior que

def calcular_lucro(venda, custo):
    return venda + custo  # MUTANTE 5: Trocou subtração por adição