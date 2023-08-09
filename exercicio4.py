#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    elementos_vistos = set()

    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False


# Teste a sua função aqui (caso ache necessário)
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 4, 5]

print(tem_duplicados(lista1))
print(tem_duplicados(lista2))










