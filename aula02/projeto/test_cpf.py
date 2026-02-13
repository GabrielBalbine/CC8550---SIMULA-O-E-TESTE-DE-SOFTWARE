import pytest
from cpf import validar_cpf, formatar_cpf


LISTA_VALIDOS = [
    "52998224725",  # Padrão
    "00000000191",  # Com zeros
    "12345678909",  # Sequência válida
]

LISTA_INVALIDOS = [
    "11111111111",  # Dígitos iguais 
    "12345678900",  # Dígito verificador errado
    "123",          # Curto
    "1234567890123",# Longo
    "abc12345678",  # Letras
    "",             # Vazio
    None            # None
]


# 2. FIXTURES 

@pytest.fixture
def cpfs_validos():
    return LISTA_VALIDOS

@pytest.fixture
def cpfs_invalidos():
    return LISTA_INVALIDOS


# 3. TESTES DE VALIDAÇÃO 

# um teste para cada cpf válido 
@pytest.mark.parametrize("cpf", LISTA_VALIDOS)
def test_validar_cpfs_reais(cpf):
    assert validar_cpf(cpf) is True

@pytest.mark.parametrize("cpf", LISTA_INVALIDOS)
def test_validar_cpfs_ruins(cpf):
    # string pra cpf vida toda
    assert validar_cpf(str(cpf)) is False


# 4. TESTES DE FORMATAÇÃO 

def test_formatar_cpf_com_sucesso(cpfs_validos):
    # Arrange
    cpf_entrada = cpfs_validos[0] 
    esperado = "529.982.247-25"
    
    # Act
    resultado = formatar_cpf(cpf_entrada)
    
    # Assert
    assert resultado == esperado

def test_nao_deve_formatar_cpf_invalido():
    # Teste de Exceção
    cpf_ruim = "11111111111"
    
    with pytest.raises(ValueError) as error:
        formatar_cpf(cpf_ruim)
    
    assert "CPF inválido" in str(error.value)