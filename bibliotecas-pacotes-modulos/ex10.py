# Importe a biblioteca pandas, leia um arquivo CSV (por exemplo, "dados.csv") e
# exiba as primeiras linhas do DataFrame.

import pandas as pd

df = pd.read_csv('dataset.csv')
print(df.head())