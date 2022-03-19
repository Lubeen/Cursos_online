'''Atividade 2 - Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e
o valor da multa por dia de atraso (ex. R$ 0,25).'''


def calculo_divida(valor, dias):
    if valor >= 2000:
        taxa = 5
    
    elif valor <= 1999:
        taxa = 2.5

    multa = dias * taxa
    divida = valor + multa

    return divida


# Programa principal
valor_original = int(input('Qual o valor original da dívida? '))
dias_atraso = int(input('Quantos dias está em atraso? '))
valor_quitacao = calculo_divida(valor_original, dias_atraso)
print(f'O valor para quitação atualizado com juros fica {valor_quitacao:.2f}')