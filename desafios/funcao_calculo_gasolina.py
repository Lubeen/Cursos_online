'''Atividade 1 - Escrever um algoritmo e um programa para efetuar o cálculo da quantidade de litros de
 combustível gastos em uma viagem, utilizando-se um automóvel que faz 12 km por litro.
 Para obter o cálculo, o usuário deverá fornecer o tempo gasto na viagem e a velocidade média durante a mesma.
 Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
  Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula
  : LITROS_USADOS = DISTANCIA / 12. O programa deverá apresentar a distância percorrida e a quantidade de litros de combustível utilizados na viagem.'''


def calculo_gasolina(tempo, velocidade):
    distancia = tempo * velocidade
    litros_usados = distancia / 12
    resposta = {'distancia':distancia,'litros_usados':litros_usados}
    return resposta




# Programa principal
tempo = float(input('Qual foi a duração da viagem?'))
velocidade = float(input('Qual foi a velocidade média da viagem? '))
custo_viagem = calculo_gasolina(tempo, velocidade)
print(f'A distancia percorrida foi de {custo_viagem["distancia"]:.2f}km e a quantidade de litros foram de {custo_viagem["litros_usados"]:.2f}')


