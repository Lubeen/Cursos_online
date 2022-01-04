peso = float(input('Digite seu peso Kg '))
altura = float(input('Digite sua altura (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f} '.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso')
elif 18.5 < imc < 25:
    print('parabens, voce esta na faixa de peso ideal')
elif 25 < imc < 30:
    print('Voce esta em sobrepeso')
elif 30 < imc < 40:
    print('Voce esta obesidade, cuidado!')
elif imc >= 40:
    print('Voce esta em obesidade morbida, cuidado!')
