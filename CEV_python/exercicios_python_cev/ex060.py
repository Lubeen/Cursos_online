'''import math
print('Calculo de fatorial')
fatorial = int(input('Digite o numero que voce quer calcular: '))
n = math.factorial(fatorial)
print('O fatorial é {}'.format(n))'''

'''c = int(input('Digite um numero'))
f = 1
print('Calculando {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
    f *= c'''
v = 1
c = int(input('Digite o numero para fatorial: '))
for f in range(c,0,-1):
    print('{}'.format(f), end=' ')
    print(' x ' if f > 1 else ' = ', end='')
    v *= f
print('{}'.format(v))