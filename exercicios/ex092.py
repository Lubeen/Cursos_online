'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o
ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from random import randint
from datetime import datetime
trabalhador = {}
trabalhador['nome'] = input('Nome: ')
ano = int(input('ano de nascimento: '))
trabalhador['idade'] = 2022 - ano
trabalhador['carteira'] = int(input('Carteira de trabalho (0 nao tem)'))
if trabalhador['carteira'] != 0:
    trabalhador['ano_contratacao'] = int(input('Ano de contratacao: '))
    trabalhador['Salario'] = float(input('Salario: R$ '))
    trabalhador['aposentadoria'] = (trabalhador['ano_contratacao'] + 35) - ano
for k, v in trabalhador.items():
    print(f'{k} é {v}')
