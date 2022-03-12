'''No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
   Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
   incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jogador = {}
gol = total = cont = 0
lista = []
jogadores = []
while True:
    jogador.clear()
    jogador['nome'] = input('nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for partida in range(0,  tot):
        gol = int(input(f'Quantos gols foram marcados na partida {partida+1}: '))
        lista.append(gol)

    jogador['gols'] = lista[:]
    jogador['total'] = sum(lista)
    jogadores.append(jogador.copy())

    lista.clear()
    total = 0
    resp = ' '
    while resp not in 'SN':
        resp = input('Voce quer continuar? [S/N]').upper().strip()[0]
        if resp == 'N':
            break
    if resp == 'N':
        break

print('=-' * 20)
print('cod  ', end=' ')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('=-' * 20)
for pos, v in enumerate(jogadores):
    print(f'{pos:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('=-' * 20)


'''for c in jogadores:
    for k, v in c.items():
        print(f'O campo {k} tem o valor {v}')'''


'''for jogador_atual in jogadores:
    print(f' O jogador {jogador_atual["nome"]} jogou {jogador_atual["partidas"]} partidas')
    for pos, v in enumerate(jogador_atual["gols"]):
        print(f'Na partida {pos+1} ele fez {v} gols')
    print(f'No total foram {jogador_atual["total"]} gols')'''
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if busca == 999:
        break
    if busca >=  len(jogadores):
        print(f'ERRO! nao existe jogador com codigo {busca}')
    else:
        print(f' ----- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'        No jogo {i+1} fez {g} gols ')
print('VOLTE SEMPRE!')

