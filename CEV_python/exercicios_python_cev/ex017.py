'''num = float(input('Digite o comprimento do cateto oposto : '))
num2 = float(input('Digite o comprimento do cateto adjacente : '))
hip = (num ** 2 + num2 ** 2) ** (1/2)  raiz quadrada
print('Com o comprimento de {} do cateto oposto e o comprimento de {} do cateto adjacente temos o resultado {:.2f} da hipotenusa'
      .format(num,num2,hip))'''
'''from math import sqrt
co = float(input('Digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente : '))
hi = co ** 2 + ca ** 2
print('com cateto oposto {} e o adjacente {} temos o resultado da hipotenusa que é {:.2f}'.format(co,ca,sqrt(hi)))'''
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente : '))
hi = math.hypot(co,ca)
print('com cateto oposto {} e o adjacente {} temos o resultado da hipotenusa que é {:.2f}'.format(co,ca,hi))
