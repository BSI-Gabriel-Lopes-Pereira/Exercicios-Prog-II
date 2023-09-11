# Crie um programa que copie o conteúdo do arquivo "texto.txt" para um novo
# arquivo chamado "copia.txt".

with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

with open('copia.txt', 'w') as arquivo:
    arquivo.write(conteudo)