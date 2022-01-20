'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou.
  Depois vai ler a quantidade de gols feitos em cada partida.
   No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = {}
gol = gols = 0
lista = []
jogador['nome'] = input('nome: ')
jogador['partidas'] = int(input('Quantas partidas? '))
for c in range(0, jogador['partidas']):
    gol = int(input(f'Quantos gols foram marcados na partida {c+1}: '))
    lista.append(gol)
    gols += gol
jogador['gols'] = gols
print(jogador)


