# Maior Valor em Dicionário de Dicionários
# Encontre a chave e valor com o maior valor em um dicionário de dicionários.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 4, "b": 5, "c": 6}
d3 = {"a": 7, "b": 8, "c": 9, "d": 10, "e": 11, "f": 12, "g": 13, "h": 14}
d4 = {"a": 15, "b": 16, "c": 17, "d": 18, "e": 19, "f": 20, "g": 21, "h": 22}

d = {"d1": d1, "d2": d2, "d3": d3, "d4": d4}

print(max(d, key = lambda x: max(d[x].values())))

