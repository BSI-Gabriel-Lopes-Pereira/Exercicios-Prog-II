# Concatenar elementos de sub-listas em uma única lista

sublists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([element for sublist in sublists for element in sublist])