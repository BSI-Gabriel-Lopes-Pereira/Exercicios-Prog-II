# Criar um dicionário a partir de duas listas

lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
#
print({lista1[i]: lista2[i] for i in range(len(lista1))})