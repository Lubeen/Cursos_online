'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
 tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
  No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
'''from random import randint
jogador = {}
maior = 0
jogador['jogador1'] = randint(1, 6)
jogador['jogador2'] = randint(1, 6)
jogador['jogador3'] = randint(1, 6)
jogador['jogador4'] = randint(1, 6)
for v in jogador.values():
    if maior < v:
        maior = v
print(f'Os numeros sorteados do menor para o maior foram {sorted(jogador.values())}')
for k, v in jogador.items():
    if maior == v:
        print(f'O vencedor foi {k} tirou {v} no dado')'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('VALORES SORTEADOS:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(0.5)

