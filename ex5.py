# Crie uma função que remova uma pessoa do dicionário.

from ex1 import pessoas

def remover_pessoa(pessoas, nome):
    if nome in pessoas:
        del pessoas[nome]
        print('Pessoa removida com sucesso')
    else:
        print('Pessoa não encontrada')
    return pessoas

print(remover_pessoa(pessoas, 'Lucas Antonete'))