# Crie um programa que peça ao usuário para digitar uma senha com pelo menos 8
# caracteres. Trate exceções caso a senha seja muito curta.

def senha():
    try:
        senha = input('Digite uma senha com pelo menos 8 caracteres: ')
        if len(senha) < 8:
            raise ValueError
        print('Senha aceita.')
    except ValueError:
        print('Senha muito curta.')

senha()