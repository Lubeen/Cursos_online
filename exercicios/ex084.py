princ = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    princ.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foram cadastradas {len(princ)} pessoas no sistema.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{[p[0]]}', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{[p[0]]}', end='')
