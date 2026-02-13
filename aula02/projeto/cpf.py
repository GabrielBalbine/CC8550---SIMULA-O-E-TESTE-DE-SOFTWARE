import re

def validar_cpf(cpf: str) -> bool:
    #remove tudo que não for número (pontos e traços)
   
    cpf = re.sub(r'[^0-9]', '', str(cpf))
    
    #tem que ter 11 dígitos
    if len(cpf) != 11:
        return False
        
    
    # se todos os dígitos forem iguais, retornamos False
    if cpf == cpf[0] * len(cpf):
        return False
        
    # digito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto
    
    if digito_1 != int(cpf[9]):
        return False
        
    # 2° digito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
        
    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto
    
    if digito_2 != int(cpf[10]):
        return False
        
    # chegou até aqui é gg
    return True

def formatar_cpf(cpf: str) -> str:
 
    # limpeza pra lidar só com números
    cpf_limpo = re.sub(r'[^0-9]', '', str(cpf))
    
    # valida com a funcao de cima
    if not validar_cpf(cpf_limpo):
        raise ValueError("CPF inválido não pode ser formatado")
    
    # transforma no formato padrão de cpf
    return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"