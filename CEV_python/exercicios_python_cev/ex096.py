'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
 que receba as dimensões de um terreno retangular (largura e comprimento) e
  mostre a área do terreno.'''
def area(a, b):
    tot = a * b
    print(f'O resultado entre {a} x {b} é {tot:.2f} m²')


# Programa principal
print('Calculo da area com comprimento e altura')
c = float(input('Qual o comprimento?'))
al = float(input('Qual a altura?'))
area(c, al)