'''Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade em um arquivo de texto simples.

O sistema só vai ter 2 opções:cadastrar uma nova pessoa e
listar todas as pessoas cadastradas.
'''


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


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opcao: ')
    return opc

