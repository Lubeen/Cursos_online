from time import sleep
numero_par = []
numero_impar = []
numeros = [2,5,6,8,4,5,1,5,58,69,42,89,63,14,584,458,972,625,14,87,52,69,18,56,898,47,12,3,6,5,6,8]
for c in range(1,50+1):
    if c % 2 == 0:
        numero_par.append(c)
    else:
        numero_impar.append(c)
print('Os numeros pares são {}'.format(numero_par))
sleep(0.5)
print('Os numeros impares são  {}'.format(numero_impar))
sleep(0.5)
