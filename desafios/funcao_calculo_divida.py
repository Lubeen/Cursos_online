'''Atividade 2 - Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e
o valor da multa por dia de atraso (ex. R$ 0,25).'''


def calculo_divida(valor, dias, taxa):
    multa = dias_atraso * taxa
    divida = valor_original + multa
    return divida



# Programa principal
valor_original = float(input('Qual o valor original da dívida? '))
dias_atraso = float(input('Quantos dias está em atraso? '))
taxa = input('Qual o valor da taxa por dia? '.replace(",", "."))
if taxa.isnumeric() and ',' in taxa:
    taxa = float()

valor_quitacao = calculo_divida(valor_original, dias_atraso, taxa)
print(f'O valor para quitação atualizado com juros fica {valor_quitacao:.2f}')