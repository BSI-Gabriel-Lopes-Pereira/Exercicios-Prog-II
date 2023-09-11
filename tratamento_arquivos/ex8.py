# Crie um programa que adicione a frase "Isso é incrível!" ao final do arquivo
# "texto.txt".

with open('texto.txt', 'a') as arquivo:
    arquivo.write('Isso é incrível!\n')