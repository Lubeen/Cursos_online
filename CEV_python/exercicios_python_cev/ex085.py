princ = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite n°{c} valor:')))
    if valor % 2 == 0:
        princ[0].append(valor)
    else:
        princ[1].append(valor)
print(f'A lista de todos os valores é {princ}')
print(f'A lista dos numeros pares em ordem crescente é {sorted(princ[0])}')
print(f'A lista dos numeros impares em ordem crescente é {sorted(princ[1])}')
