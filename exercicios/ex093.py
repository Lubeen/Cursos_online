'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou.
  Depois vai ler a quantidade de gols feitos em cada partida.
   No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = {}
gol = total = 0
lista = []
jogador['nome'] = input('nome do jogador: ')
partidas = int(input('Quantas partidas? '))
for c in range(0, partidas):
    gol = int(input(f'Quantos gols foram marcados na partida {c}: '))
    lista.append(gol)
    total += gol
jogador['gols'] = lista[:]
jogador['total'] = total
print(jogador)
print('=-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for pos, v in enumerate(lista):
    print(f'    => Na partida {pos}, fez {v} gols.')
print(f'Foi um total de {total} gols.')

