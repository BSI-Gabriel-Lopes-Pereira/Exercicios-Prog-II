# Escreva um programa que divida uma lista em partes iguais e trate exceções se o
# número de partes não for válido.

def divide(lista, n):
    try:
        return [lista[i:i + n] for i in range(0, len(lista), n)]
    except Exception:
        print("Número de partes inválido")

print(divide([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))