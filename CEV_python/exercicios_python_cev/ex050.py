soma = 0
for c in range (1,6):
    numeros =int(input('Digite um numero: '))
    if numeros % 2 == 0:
        soma += numeros
    else:print('Desconsiderado')
print('A soma dos numeros pares é {}'.format(soma))