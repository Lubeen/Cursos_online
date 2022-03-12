'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
 Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} a {f} de {p} em {p}')

    if i < f:
        cont = i
        print(f'=-' * 20)
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        print(f'=-' * 20)
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= p
        print(f'FIM!')


# Codigo principal
contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é sua vez de personalizar!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)






