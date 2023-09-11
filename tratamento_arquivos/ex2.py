# Crie um programa que leia o conteúdo do arquivo "texto.txt" criado no
# exercício anterior e o exiba no console.

with open('texto.txt', 'r') as file:
    print(file.read())