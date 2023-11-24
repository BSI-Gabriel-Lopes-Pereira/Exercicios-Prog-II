# Escreva um código que tente abrir um arquivo com o modo de escrita, porém o
# arquivo já existe. Se ocorrer uma exceção, imprima uma mensagem de erro.

try:
    with open('world.txt', 'w') as file:
        file.write('Olá, mundo!')
except FileExistsError:
    print('Arquivo já existe')