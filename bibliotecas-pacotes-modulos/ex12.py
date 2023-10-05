# Escreva um programa que importe o pacote beautifulsoup4 e faça a raspagem
# de dados (web crawling) de uma página HTML.

from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com.br'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())