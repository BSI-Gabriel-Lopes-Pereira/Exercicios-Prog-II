# Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de
# nomes, mas sem as vogais.

# function to remove vowels from a string

def remove_vowels(string):
    vowels = 'aeiou'
    return ''.join([letter for letter in string if letter not in vowels])

names = ['maria', 'josé', 'pedro', 'joão', 'mateus', 'luiz', 'carlos', 'ana', 'amanda', 'bruna', 'gabriel', 'gustavo', 'fernanda', 'felipe', 'daniel', 'larissa', 'luis', 'mario', 'miguel', 'patricia', 'paulo', 'rafael', 'ricardo', 'rodrigo', 'sandra', 'sara', 'tatiana', 'thiago', 'vitor', 'andré', 'juliana']

print([remove_vowels(name) for name in names[:10]])