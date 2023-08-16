# Crie uma função que receba um nome e uma nova idade como parâmetros e
# atualize a idade da pessoa correspondente no dicionário.

from ex1 import pessoas

def atualiza_idade(nome, idade):
    pessoas[nome] = idade
    return pessoas

print(atualiza_idade('João Felipi', 20))
