# Escreva um programa que contenha um loop infinito e trate exceções para permitir
# ao usuário interrompê-lo.

while True:
    try:
        print('Loop infinito')
    except KeyboardInterrupt:
        print('Loop interrompido')
        break