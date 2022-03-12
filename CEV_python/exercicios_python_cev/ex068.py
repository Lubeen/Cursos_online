from random import randint
vitoria = 0
while True:
    num = int(input('Digite um numero: '))
    numpc = randint(0, 50)
    soma = num + numpc
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Voce escolhe par ou impar [P/I] ?')).strip().upper()
    print(f'Voce jogou {num} e o computador jogou {numpc}, a soma dos dois é {soma}')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Voce venceu')
            vitoria += 1
        else:
            print('Voce perdeu')
            break
    elif opcao == 'I':
        if soma % 2 == 1:
            print('Voce venceu')
            vitoria += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game over, voce venceu {vitoria} vezes!')
