# Crie uma lista com os números primos de 1 a 20. Dica: use uma função para
# verificar se o número é primo ou não.

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

primes = [number for number in range(1, 21) if is_prime(number)]
print(primes)