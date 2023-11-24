# Escreva uma função que recebe uma string como argumento e retorna o número
# de vogais contidas nessa string. Use um bloco `try/except` para tratar o caso em
# que o argumento não é uma string e lance uma exceção personalizada com a
# mensagem “Argumento inválido”.

def vogais(string):
    try:
        return len([c for c in string.lower() if c in "aeiou"])
    except AttributeError:
        raise Exception("Argumento inválido")

print(vogais("Python"))