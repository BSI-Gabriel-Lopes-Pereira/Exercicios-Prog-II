# Escreva uma função que recebe uma lista de números como argumento e retorna a
# soma dos elementos da lista. Use um bloco `try/except` para tratar o caso em que
# a lista contém algum elemento que não é um número e lance uma exceção
# personalizada com a mensagem “Lista inválida”.

def soma(lista):
    try:
        return sum(lista)
    except TypeError:
        raise Exception("Lista inválida")

print(soma([1, 2, 3]))