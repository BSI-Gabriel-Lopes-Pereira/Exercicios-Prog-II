# Crie um programa que conte e exiba o número de palavras no arquivo
# "texto.txt".

with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    print(len(palavras))