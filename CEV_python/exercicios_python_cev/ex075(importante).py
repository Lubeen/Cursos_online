tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite e outro valor: ')),
         int(input('Digite mais um valor: ')))
print(f'voce digitou {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na posicao {tupla.index(3)}')
else:
    print('O valor 3 não foi digitado')
print(f'Os numeros pares foram ', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')

