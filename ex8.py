# Crie uma função que retorne a pessoa mais velha do dicionário.

from ex1 import pessoas

def mais_velha(pessoas):
    return max(pessoas, key=pessoas.get)

print(mais_velha(pessoas))