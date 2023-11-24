# Escreva uma função que recebe um número inteiro positivo como argumento e
# retorna o fatorial desse número. Use um bloco `try/except` para tratar o caso em
# que o argumento é negativo ou não é um inteiro e lance uma exceção
# personalizada com a mensagem “Argumento inválido”.

def fatorial(n):
    try:
        if n < 0:
            raise Exception("Argumento inválido")
        if n == 0:
            return 1
        return n * fatorial(n - 1)
    except TypeError:
        raise Exception("Argumento inválido")

print(fatorial(5))