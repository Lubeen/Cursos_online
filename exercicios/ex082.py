par = []
lista = []
impar = []
while True:
    lista.append(int(input('Digite um valor qualquer :')))
    r = ' '
    while r not in 'NS':
        r = input('Voce quer continuar? [S/N]').upper().strip()[0]
    if r == 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares foram {par}')
print(f'Os valores impares foram {impar}')
