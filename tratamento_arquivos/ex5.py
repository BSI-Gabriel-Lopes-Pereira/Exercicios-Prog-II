# Crie um programa que leia o conteúdo dos arquivos "texto.txt" e
# "copia.txt", e escreva o conteúdo combinado em um terceiro arquivo
# chamado "combinado.txt".

with open('texto.txt', 'r') as arquivo:
    conteudo_texto = arquivo.read()

with open('copia.txt', 'r') as arquivo:
    conteudo_copia = arquivo.read()

with open('combinado.txt', 'w') as arquivo:
    arquivo.write(conteudo_texto + conteudo_copia)