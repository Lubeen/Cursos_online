print('Calcule a quantidade de tinta necessaria para pintar')
al =float(input('Digite a altura: '))
lar =float(input ('Digite a largura :'))
area = al * lar
print('Com a altura de {:.2f}m e a largura de {:.2f}m conseguimos a area de {:.2f}m²'.format(al,lar,area))
tinta = area / 2
print('A quantidade de tinta necessaria é {:.2f} litros'.format(tinta))