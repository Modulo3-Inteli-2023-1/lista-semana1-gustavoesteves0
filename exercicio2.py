#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def cumulativo(lista):
    cumulativa = []
    soma = 0
    for num in lista:
        soma += num
        cumulativa.append(soma)
    return cumulativa





# Teste a sua função aqui (caso ache necessário)
lista = [2, 3, 4, 5]
resultado = cumulativo(lista)
print(resultado)










