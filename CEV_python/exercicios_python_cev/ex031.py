distancia = float(input('Digite a distancia em km : '))
print('Voce esta prestes a comecar uma viagem de {:.2f}km'.format(distancia))
if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço de sua passagem sera de R${:.2f} reais'.format(preço))