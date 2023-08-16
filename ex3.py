# Crie uma função que receba um nome como parâmetro e retorne a idade da
# pessoa correspondente no dicionário.

from ex1 import pessoas

def idade(nome):
    return pessoas[nome]

print(idade('João Felipi'))