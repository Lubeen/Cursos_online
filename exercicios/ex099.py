'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
 que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

# parametros empacotados
def maior(* num):
    cont = maior = 0
    print('\n Analisando os valores passados... ')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        cont += 1
    print(f' Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
