# Crie uma função que retorne uma lista com as pessoas cujo nome começa com a
# letra "J".

from ex1 import pessoas

def comeca_com_j(pessoas):
    return [pessoa for pessoa in pessoas if pessoa[0] == 'J']

print(comeca_com_j(pessoas))