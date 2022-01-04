velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('Siga em frente!')
else: print('Você foi multado em R${:.2f} reais'.format(multa))

