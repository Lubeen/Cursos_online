lista = []
cont = 0
while True:
    num = int(input('Digite um valor'))
    if cont == 0 or num < lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos <= len(lista):
            if num >= lista[pos]:
                lista.insert(pos, num)
            break
        pos += 1
    c = ' '
    cont += 1
    while c not in 'SN':
        c = input('Voce quer continuar ? [S/N]').strip().upper()[0]
    if c == 'N':
        break
if 5 in lista:
    print(f'O valor 5 foi digitado ')
else:
    print(f'O valor 5 nao foi digitado!')
print(f'A quantidade de numeros digitados foi {len(lista)}')
print(f'A lista em ordem decrescente é {lista}')
