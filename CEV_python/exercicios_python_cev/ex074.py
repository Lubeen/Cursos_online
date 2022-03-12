from random import randint
tupla = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))
print('Os numeros gerados foram', end=' ')
for numero in tupla :
    print(f' {numero}', end=' ')
print(f'\nO maior numero da tupla foi {max(tupla)}')
print(f'O menor valor da tupla foi {min(tupla)}')
