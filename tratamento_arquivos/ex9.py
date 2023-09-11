# Crie um programa que leia o conteúdo do arquivo "texto.txt" e conte quantas
# letras (excluindo espaços) estão presentes no texto.

with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    letras = conteudo.replace(' ', '')
    print(len(letras))