'''Exercício Python 089: Crie um programa
que leia nome e duas notas de vários alunos e
 guarde tudo em uma lista composta. No final,
 mostre um boletim contendo a média de cada um
 e permita que o usuário possa mostrar as notas
 de cada aluno individualmente.'''
'''alunos = []
lista = []
media = 0
ver = 0
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    media = (nota1 + nota2) / 2
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    r = ' '
    while r not in 'S/N':
        r = input('Voce quer continuar? [S/N]').upper().strip()[0]
    if r == 'N':
        break
print('-=' * 30)
print('No.  Nome      Média')
for pos, var in enumerate(alunos):
    print(f'[{pos}] {alunos[pos][0]:^10}  {alunos[pos][3]}
')
print('-' * 30)
while ver != 999:
    ver = int(input('Qual aluno voce quer ver as notas? [999] para parar: '))
    for pos, var in enumerate(alunos):
        if ver == pos:
            print(f'{alunos[pos][0]} as notas foram de {alunos[pos][1]} e {alunos[pos][2]}')
print('Volte sempre')'''
lista = []
opc = 0
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('mostrar notas de qual aluno? [999 interrompe]'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista)-1:
        print(f'Notas de {lista[opc][0]} sao {lista[opc][1]}')
print('Volte sempre')