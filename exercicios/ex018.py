'''print('Calculo de angulo para cos, seno e tangente')
import math
angulo = float(input('Digite o angulo : '))
cos = math.cos(math.radians(angulo))
print('O angulo de {} corresponde ao cosseno de {:.2f}'.format(angulo,cos))
seno = math.sin(math.radians(angulo))
print('O angulo de {} corresponde ao seno de {:.2f}'.format(angulo,seno))
tan = math.tan(math.radians(angulo))
print('O angulo de {} corresponde a tangente de {:.2f}'.format(angulo,tan))'''
print('Calculo de angulo para cos, seno e tangente')
from math import cos,sin,tan,radians
angulo = float(input('Digite o angulo : '))
cos = cos(radians(angulo))
print('O angulo de {} corresponde ao cosseno de {:.2f}'.format(angulo,cos))
seno = sin(radians(angulo))
print('O angulo de {} corresponde ao seno de {:.2f}'.format(angulo,seno))
tan = tan(radians(angulo))
print('O angulo de {} corresponde a tangente de {:.2f}'.format(angulo,tan))