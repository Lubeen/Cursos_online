contnum = soma = num = 0
num = int(input('Digite qualquer numero [999 para parar]'))
while num != 999:
    soma += num
    contnum += 1
    num = int(input('Digite qualquer numero'))
print(' o total de numeros digitados foram {} e a soma entre eles é {}'.format(contnum,soma))