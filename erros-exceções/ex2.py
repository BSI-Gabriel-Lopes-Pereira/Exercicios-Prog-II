# Escreva um programa que solicita ao usuário uma data no formato "dd/mm/aaaa"
# e verifica se ela é válida. Use um bloco `try/except` para tratar o caso em que o
# usuário digita uma data inválida e lance uma exceção personalizada com a
# mensagem “Data inválida”.

def data_valida(data):
    try:
        dia, mes, ano = data.split('/')
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if dia < 1 or dia > 31:
            return False
        if mes < 1 or mes > 12:
            return False
        if ano < 1:
            return False
        return True
    except ValueError:
        return False

data = input('Digite uma data no formato "dd/mm/aaaa": ')
if data_valida(data):
    print('Data válida')
else:
    print('Data inválida')
