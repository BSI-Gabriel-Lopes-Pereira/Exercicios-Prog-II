# Escreva um programa que solicita ao usuário um nome de arquivo e tenta abri-lo
# para leitura. Use um bloco `try/except` para tratar o caso em que o arquivo não
# existe ou não pode ser aberto e lance uma exceção personalizada com a
# mensagem “Arquivo inválido”.

def le_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        raise Exception('Arquivo inválido')

nome_arquivo = input('Digite o nome do arquivo: ')
try:
    conteudo = le_arquivo(nome_arquivo)
    print(conteudo)
except Exception as e:
    print(e)