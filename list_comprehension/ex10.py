# Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de
# nomes, mas com as primeiras letras maiúsculas.

names = ['maria', 'josé', 'pedro', 'joão', 'mateus', 'luiz', 'carlos', 'ana', 'amanda', 'bruna', 'gabriel', 'gustavo', 'fernanda', 'felipe', 'daniel', 'larissa', 'luis', 'mario', 'miguel', 'patricia', 'paulo', 'rafael', 'ricardo', 'rodrigo', 'sandra', 'sara', 'tatiana', 'thiago', 'vitor', 'andré', 'juliana']

print([name.capitalize() for name in names[:10]])