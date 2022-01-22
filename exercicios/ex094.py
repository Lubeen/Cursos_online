'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
 guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
  No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
  C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''
pessoa = {}
lista = []
media = 0
listam = []
mediaidade = []
while True:
    pessoa = {'nome': input('Nome: '),
              'idade': int(input('Idade:'))}
    while True:
        pessoa['sexo'] = input('Sexo[M/F] ').upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apens M ou F.')
    if pessoa['sexo'] == 'F':
        listam.append(pessoa.copy())
    media += pessoa['idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        r = input('Voce quer continuar? [S/N]').upper().strip()[0]
        if r in 'SN':
            break
        print('[ERROR] por favor, escreva [S/N]')
    if r == 'N':
        break
media = media / len(lista)
for pos, v in enumerate(lista):
    if lista[pos]['idade'] >= media:
        mediaidade.append(lista[pos])
print(lista)
print(f'A quantidade de pessaos cadastradas foram {len(lista)}')
print(f'A media de idade é {media:.2f}')
print(f'A lista de mulheres é {listam}')
print(f' A lista de pessoas com idade maior que a media {mediaidade}')


