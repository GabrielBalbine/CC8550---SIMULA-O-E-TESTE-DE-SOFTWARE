from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
def calcular_total(preco, quantidade):
    args = [preco, quantidade]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_calcular_total__mutmut_orig, x_calcular_total__mutmut_mutants, args, kwargs, None)
def x_calcular_total__mutmut_orig(preco, quantidade):
    return preco / quantidade  # MUTANTE 1: Trocou multiplicação por divisão
def x_calcular_total__mutmut_1(preco, quantidade):
    return preco * quantidade  # MUTANTE 1: Trocou multiplicação por divisão

x_calcular_total__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_calcular_total__mutmut_1': x_calcular_total__mutmut_1
}
x_calcular_total__mutmut_orig.__name__ = 'x_calcular_total'

def tem_estoque(estoque_atual, quantidade_desejada):
    args = [estoque_atual, quantidade_desejada]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_tem_estoque__mutmut_orig, x_tem_estoque__mutmut_mutants, args, kwargs, None)

def x_tem_estoque__mutmut_orig(estoque_atual, quantidade_desejada):
    return estoque_atual > quantidade_desejada  # MUTANTE 2: Tirou o "igual" do maior ou igual

def x_tem_estoque__mutmut_1(estoque_atual, quantidade_desejada):
    return estoque_atual >= quantidade_desejada  # MUTANTE 2: Tirou o "igual" do maior ou igual

x_tem_estoque__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_tem_estoque__mutmut_1': x_tem_estoque__mutmut_1
}
x_tem_estoque__mutmut_orig.__name__ = 'x_tem_estoque'

def aplicar_desconto(valor, cupom):
    args = [valor, cupom]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_aplicar_desconto__mutmut_orig, x_aplicar_desconto__mutmut_mutants, args, kwargs, None)

def x_aplicar_desconto__mutmut_orig(valor, cupom):
    if cupom != "PHOBIA_VIP":  # MUTANTE 3: Trocou "==" por "!="
        return valor * 0.8
    return valor

def x_aplicar_desconto__mutmut_1(valor, cupom):
    if cupom == "PHOBIA_VIP":  # MUTANTE 3: Trocou "==" por "!="
        return valor * 0.8
    return valor

def x_aplicar_desconto__mutmut_2(valor, cupom):
    if cupom != "XXPHOBIA_VIPXX":  # MUTANTE 3: Trocou "==" por "!="
        return valor * 0.8
    return valor

def x_aplicar_desconto__mutmut_3(valor, cupom):
    if cupom != "phobia_vip":  # MUTANTE 3: Trocou "==" por "!="
        return valor * 0.8
    return valor

def x_aplicar_desconto__mutmut_4(valor, cupom):
    if cupom != "PHOBIA_VIP":  # MUTANTE 3: Trocou "==" por "!="
        return valor / 0.8
    return valor

def x_aplicar_desconto__mutmut_5(valor, cupom):
    if cupom != "PHOBIA_VIP":  # MUTANTE 3: Trocou "==" por "!="
        return valor * 1.8
    return valor

x_aplicar_desconto__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_aplicar_desconto__mutmut_1': x_aplicar_desconto__mutmut_1, 
    'x_aplicar_desconto__mutmut_2': x_aplicar_desconto__mutmut_2, 
    'x_aplicar_desconto__mutmut_3': x_aplicar_desconto__mutmut_3, 
    'x_aplicar_desconto__mutmut_4': x_aplicar_desconto__mutmut_4, 
    'x_aplicar_desconto__mutmut_5': x_aplicar_desconto__mutmut_5
}
x_aplicar_desconto__mutmut_orig.__name__ = 'x_aplicar_desconto'

def frete_gratis(valor_compra):
    args = [valor_compra]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_frete_gratis__mutmut_orig, x_frete_gratis__mutmut_mutants, args, kwargs, None)

def x_frete_gratis__mutmut_orig(valor_compra):
    return valor_compra >= 1000  # MUTANTE 4: Adicionou o "igual" no maior que

def x_frete_gratis__mutmut_1(valor_compra):
    return valor_compra > 1000  # MUTANTE 4: Adicionou o "igual" no maior que

def x_frete_gratis__mutmut_2(valor_compra):
    return valor_compra >= 1001  # MUTANTE 4: Adicionou o "igual" no maior que

x_frete_gratis__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_frete_gratis__mutmut_1': x_frete_gratis__mutmut_1, 
    'x_frete_gratis__mutmut_2': x_frete_gratis__mutmut_2
}
x_frete_gratis__mutmut_orig.__name__ = 'x_frete_gratis'

def calcular_lucro(venda, custo):
    args = [venda, custo]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_calcular_lucro__mutmut_orig, x_calcular_lucro__mutmut_mutants, args, kwargs, None)

def x_calcular_lucro__mutmut_orig(venda, custo):
    return venda + custo  # MUTANTE 5: Trocou subtração por adição

def x_calcular_lucro__mutmut_1(venda, custo):
    return venda - custo  # MUTANTE 5: Trocou subtração por adição

x_calcular_lucro__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_calcular_lucro__mutmut_1': x_calcular_lucro__mutmut_1
}
x_calcular_lucro__mutmut_orig.__name__ = 'x_calcular_lucro'