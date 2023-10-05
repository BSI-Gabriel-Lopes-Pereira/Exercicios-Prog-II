# Importe o pacote requests e faça uma requisição HTTP para um URL e exiba o
# código de status.

import requests

url = 'https://www.google.com.br'
response = requests.get(url)
print(response.status_code)