'''Faça um programa que leia a idade de uma pessoa expressa em anos,
 meses e dias e mostre-a expressa apenas em dias.'''

idade = input('Qual sua idade?')
limite = 200
if idade.isnumeric():
    idade = int(idade)
if idade < limite:
    idade_dias = idade * 365
    print(f'Voce tem {idade_dias:.2f} dias de idade')
if idade > limite:
    idade_meses = (idade / 12) * 365
    print(f'Voce tem {idade_meses:.2f} dias de idade')






