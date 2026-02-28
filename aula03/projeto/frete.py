def calcular_frete(peso: float, destino: str, valor_pedido: float) -> float:
    # 1. Regra de Ouro: Frete Grátis
    if valor_pedido > 200.00:
        return 0.0
        
    # 2. Validações de Erro (Limites absolutos)
    if peso <= 0:
        raise ValueError("Peso zero ou negativo não permitido")
    if peso > 20:
        raise ValueError("Peso acima de 20 kg não aceito")
        
    # 3. Cálculo Base por Peso
    if peso <= 1.0:
        base = 10.0
    elif peso <= 5.0:
        base = 15.0
    else:
        base = 25.0
        
    # 4. Multiplicador de Destino
    if destino == "mesma região":
        multiplicador = 1.0 # Sem acréscimo
    elif destino == "outra região":
        multiplicador = 1.5 # +50%
    elif destino == "internacional":
        multiplicador = 2.0 # +100%
    else:
        raise ValueError("Destino inválido")
        
    return base * multiplicador