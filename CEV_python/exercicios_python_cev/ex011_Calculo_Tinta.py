def calculo_tinta(altura,largura):
    area = altura * largura
    tinta = area / 2
    return tinta 

# Programa principal
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
tinta = calculo_tinta(altura,largura)
print(f'Com a altura de {altura}m e a largura de {largura}m, a tinta necessária é de {tinta} litros')
