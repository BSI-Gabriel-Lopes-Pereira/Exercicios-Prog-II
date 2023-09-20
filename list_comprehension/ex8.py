# Crie uma lista com as datas de todos os dias de janeiro em um ano bissexto
# (considerando que um ano bissexto é divisível por 4).

from datetime import date

print([date(2020, 1, day) for day in range(1, 32)])