# Crie uma função que retorne a pessoa mais nova do dicionário.

from ex1 import pessoas

def pessoa_mais_nova(pessoas):
    return min(pessoas, key=pessoas.get)

print(pessoa_mais_nova(pessoas))