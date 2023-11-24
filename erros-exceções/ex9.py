# Escreva um programa que solicite ao usuário um índice e, em seguida, tente
# acessar um elemento em uma lista. Trate exceções caso o índice esteja fora dos
# limites da lista.

def index():
    lista = [1, 2, 3, 4, 5]
    try:
        indice = int(input('Digite um índice: '))
        print(lista[indice])
    except IndexError:
        print('Índice fora dos limites da lista.')
    except ValueError:
        print('Índice inválido.')

index()