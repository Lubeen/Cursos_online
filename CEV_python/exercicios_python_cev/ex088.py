'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
 cadastrando tudo em uma lista composta.'''
'''from random import randint
r = int(input('Digite quantos jogos voce quer (max=30):'))
jogos = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for var in range(1, r+1):
    jogos[var].append(randint(1, 60))
    jogos[var].append(randint(1, 60))
    jogos[var].append(randint(1, 60))
    jogos[var].append(randint(1, 60))
    jogos[var].append(randint(1, 60))
    jogos[var].append(randint(1, 60))
print(f'A quantidade de jogos foram {r}')
for pos, c in enumerate(jogos):
    if jogos[pos] != []:
        print(f'Jogo nª{pos}:{jogos[pos]}')'''
from random import randint
lista = []
jogos = []
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'os números sorteados foram {jogos}')
for i, l in enumerate(jogos):
    print(f'jogos {i+1}:{l}')






