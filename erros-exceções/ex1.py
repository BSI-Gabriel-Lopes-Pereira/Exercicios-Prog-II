# Escreva uma função que recebe dois números como argumentos e retorna a
# divisão do primeiro pelo segundo. Use um bloco try/except para tratar o caso em
# que o segundo número é zero e lance uma exceção personalizada com a
# mensagem "Divisão por zero não permitida".

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise Exception("Divisão por zero não é permitida")

# print(div(10, 2))
print(div(10, 0))