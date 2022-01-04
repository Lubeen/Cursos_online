from time import sleep
p = 0
i = 0
numeros = [2,5,6,8,4,5,1,5,58,69,42,89,63,14,584,458,972,625,14,87,52,69,18,56,898,47,12,3,6,5,6,8]
for c in numeros:
    print(c)
    if c % 2 == 0:
        p += 1
        print('O numero {} é par'.format(c))
        sleep(0.5)
    else:
        print('O numero {} é impar'.format(c))
        i += 1
        sleep(0.5)
print('A quantidade de numeros pares foram de {}'.format(p))
print('A quantidade de numeros impares foram de {}'.format(i))
# aprendendo mecher com Git e Github em 04/01/2022
var = 0