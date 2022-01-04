from random import randint
from time import sleep
print('Vamos jogar JOKENPO')
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
itens = ('PEDRA', ' PAPEL', ' TESOURA')
computador = randint(0,2)
jogador = int(input('Digite o numero : '))
print('J0')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if computador == 0:
    print('O numero escolhido pelo computador foi {}'.format(itens[computador]))
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vencer')
    elif jogador == 2:
        print('Jogador perdeu')
    else:print('comando invalido tente novamente!')
elif computador == 1:
    if jogador == 0:
        print('Jogador ganhou!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador perdeu')
    else:print('Jogada invalida, tente novamente')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Jogador perdeu!')
    elif jogador == 2:
        print('EMPATE')
    else:print('Jogada invalida, tente novamente')
else:print('Jogada invalida')
print('A SUA JOGADA FOI {} E A JOGADA DO COMPUTADOR FOI {}'.format(itens[jogador],itens[computador]))