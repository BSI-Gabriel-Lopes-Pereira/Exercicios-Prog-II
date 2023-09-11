# Crie um programa que conte e exiba o número de linhas no arquivo
# "texto.txt".

with open('texto.txt', 'r') as file:
    print(len(file.readlines()))