# Crie uma lista com os números divisíveis por 3 e 5 de 1 a 30.

numbers = [number for number in range(1, 31) if number % 3 == 0 and number % 5 == 0]
print(numbers)