def validar_nota(nota):
    if not isinstance(nota, (int, float)):
        return False
    
    return 0 <= nota <= 10

def calcular_media(notas):
  
    #ve se a lista de notas está ou não vazia
    if not notas:
        raise ValueError("Lista vazia")
    
    #cria uma lista só com oq for validado pela função de validar notas 
    notas_validas = [n for n in notas if validar_nota(n)]
    
    #ve se tem mais algo para se calcular
    if not notas_validas:
        raise ValueError("Nenhuma nota válida para calcular")

    #operação simples de média   
    soma = sum(notas_validas)
    quantidade = len(notas_validas)
    
    return soma / quantidade    

def obter_situacao(media):

    #verifica se a nota faz de fato sentido, se ela existe
    if not validar_nota(media):
        raise ValueError("Média inválida")
        
   #regras, apenas regras
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"


def calcular_estatisticas(notas):

    #confere novamente se as notas foram validadas
    notas_validas = [n for n in notas if validar_nota(n)]
    
    #se nao tiver nada, taca zero em tudo pra nao explodir
    if not notas_validas:
        return {
            "media": 0.0, "maior": 0.0, "menor": 0.0,
            "aprovados": 0, "reprovados": 0, "recuperacao": 0
        }
    
    #matematica basica
    media = sum(notas_validas) / len(notas_validas)
    maior = max(notas_validas)
    menor = min(notas_validas)
    
   #inicia o contador que será utilizado na função abaixo 
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    
    for nota in notas_validas:
        #utiliza a mesma função de obter situação, só que agora contabilizando
        situacao = obter_situacao(nota)
        
        if situacao == "Aprovado":
            aprovados += 1
        elif situacao == "Recuperacao":
            recuperacao += 1
        elif situacao == "Reprovado":
            reprovados += 1
            
    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "reprovados": reprovados,
        "recuperacao": recuperacao
    }

def normalizar_notas(notas, nota_maxima=10):
    #array pra dale
    notas_normalizadas = []
    
    for nota in notas:
        #calcula a normalização 
        nova_nota = (nota / nota_maxima) * 10
        
        notas_normalizadas.append(round(nova_nota, 2))
        
    return notas_normalizadas