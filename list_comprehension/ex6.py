# Crie uma lista com as palavras de uma string que tenham mais de 3 letras.

string = 'Crie uma lista com as palavras de uma string que tenham mais de 3 letras.'
print([word for word in string.split() if len(word) > 3])