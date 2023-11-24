# Peça ao usuário para digitar um número inteiro e, em seguida, tente converter
# esse número em uma string. Trate a exceção que pode ocorrer.

def inteiro():
    try:
        numero = int(input('Digite um número inteiro: '))
        print(f'"{str(numero)}"')
    except ValueError:
        print('O número digitado não é inteiro.')

inteiro()