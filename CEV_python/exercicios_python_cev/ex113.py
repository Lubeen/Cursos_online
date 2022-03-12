'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função
 input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. e
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[0;31mERRO! Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[0;31mERRO! Entrada de dados interrompida pelo usuário.\033[m')
        else:
            return real


# Programa principal
n = leiaInt('Digite um numero inteiro: ')
real = leiaFloat('Digite um numero real: ')
print(f'Voce acabou de digitar o numero {n} e o {real}')

