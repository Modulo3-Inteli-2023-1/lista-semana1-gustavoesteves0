#  Se achar necessario, faça import de outras bibliotecas


# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(x, y):
    
    soma = x + y 
    subtracao = x - y 
    multiplicacao = x * y

    if y != 0:
        divisao = x / y
    else:
        divisao = 0
    return soma, subtracao, multiplicacao, divisao


# Teste a sua função aqui (caso ache necessário)
resultado = multiplas_operacoes(55, 5)
print(resultado)