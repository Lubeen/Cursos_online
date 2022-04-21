print('Conversor de moedas')

def conversor(valor, moeda):    
    if moeda == 'dol':
        return valor * 4.23
    elif moeda == 'eur':
        return valor * 4.27
    elif moeda == 'lib':
        return valor * 0.89
    elif moeda == 'yen':
        return valor * 0.0092
    elif moeda == 'real':
        return valor * 4.15
    else:
        return 'Moeda não encontrada'


# Programa principal
valor = float(input('Digite o valor: '))
moeda = input('Digite a moeda: ')
calculo = conversor(valor, moeda)
print(calculo)