# Crie um programa que leia o conteúdo do arquivo "numeros.txt" (contendo
# números inteiros separados por vírgula), some esses números e exiba o
# resultado.

with open('numeros.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    numeros = conteudo.split(',')
    soma = 0
    for numero in numeros:
        soma += int(numero)
    print(soma)