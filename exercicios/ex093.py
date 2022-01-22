'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou.
  Depois vai ler a quantidade de gols feitos em cada partida.
   No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
   Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
   incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jogador = {}
gol = total = cont = 0
lista = []
jogadores = []
while True:
    jogador['nome'] = input('nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, jogador['partidas']+1):
        gol = int(input(f'Quantos gols foram marcados na partida {c}: '))
        lista.append(gol)
        total += gol
    jogador['gols'] = lista[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    print(jogador)
    jogador.clear()
    total = 0
    lista.clear()
    resp = ' '
    while resp not in 'SN':
        resp = input('Voce quer continuar? [S/N]').upper().strip()[0]
        if resp == 'N':
            break
    if resp == 'N':
        break
print('=-' * 20)
for c in jogadores:
    for k, v in c.items():
        print(f'O campo {k} tem o valor {v}')
print('=-' * 20)
while cont < len(jogadores[0]["nome"]):
    for pos, i in enumerate(jogadores):
        print(f'O jogador {jogadores[pos]["nome"]} jogou {len(jogadores[pos]["gols"])} partidas.')
        for c in range(0, jogadores[pos]["partidas"]+1):
            print(f'    => Na partida {c}, fez {i["gols"][c]}.')
        for v in i.values():
            print(f'Foi um total de {v[3]} gols.')
    cont += 1

