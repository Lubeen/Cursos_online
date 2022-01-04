numeros = [2,5,6,8,4,5,1,5,58,69,42,89,63,14,584,458,972,625,14,87,52,69,18,56,898,47,12,3,6,5,6,8]
numeros_par = []
numeros_impa = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_par.append(numero)
    elif numero % 2 == 1:
        numeros_impa.append(numero)
print('os numeros pares sao : {}'.format(numeros_par))
print('os numeros impares sao : {}'.format(numeros_impa))