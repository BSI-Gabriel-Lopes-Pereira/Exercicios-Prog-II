# Crie uma função que retorne a média das idades das pessoas no dicionário.

from ex1 import pessoas

def media_idades(pessoas):
    soma = 0
    for pessoa in pessoas:
        soma += pessoas[pessoa]
    return soma / len(pessoas)

print(media_idades(pessoas))