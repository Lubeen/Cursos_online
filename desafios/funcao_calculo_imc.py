'''Tendo como dados de entrada a altura e o sexo de uma pessoa, construa
um algoritmo para calcular seu peso ideal, utilizando as seguintes fórmulas:
- para homens: 72,7 * altura – 58
- para mulheres: 62,1 * altura – 44,7'''



def Calculo_imc(altura, peso, sexo):
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
    return imc


# Programa principal
altura = float(input('Qual sua altura ?'))
sexo = ' '
peso = float(input('Digite seu peso? '))
while sexo not in 'MF':
    sexo = input('Qual seu sexo ? [M/F]').upper().strip()[0]
resposta = Calculo_imc(altura, peso, sexo)



