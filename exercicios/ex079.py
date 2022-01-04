lista = []
while True:
    num = int(input('Digite um numero qualquer: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, nao vou adicionar!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Voce quer continuar [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print(f'{sorted(lista)}')
