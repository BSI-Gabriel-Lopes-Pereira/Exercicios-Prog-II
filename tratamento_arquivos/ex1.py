# Crie um programa que crie um arquivo chamado "texto.txt" e escreva nele o
# seguinte texto: "Olá, mundo!"

with open('texto.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!\n')