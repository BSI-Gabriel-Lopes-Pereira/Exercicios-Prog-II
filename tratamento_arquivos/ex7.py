# Crie um programa que leia o conteúdo do arquivo "texto.txt" e substitua
# todas as ocorrências da palavra "mundo" por "Python". O novo conteúdo deve ser
# escrito em um novo arquivo chamado "modificado.txt".

with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

conteudo = conteudo.replace('mundo', 'Python')

with open('modificado.txt', 'w') as arquivo:
    arquivo.write(conteudo)