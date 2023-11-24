# Escreva uma função que recebe uma lista de strings como argumento e retorna
# uma nova lista com estas strings ordenadas alfabeticamente. Use um bloco
# `try/except` para tratar o caso em que a lista contém algum elemento que não é
# uma string e lance uma exceção personalizada com a mensagem “Lista inválida”.

def ordena(lista):
    try:
        return sorted(lista)
    except TypeError:
        raise Exception("Lista inválida")

print(ordena(["Python", "Java", "C++"]))