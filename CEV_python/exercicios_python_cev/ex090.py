'''Exercicio Python 090: faça um programa que leia nome e
 média de um aluno, guardando também a situação em um dicionário.
  No final, mostre o conteúdo da estrutura na tela.'''
aluno = {}
dados = []
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
dados.append(aluno.copy())
print('-=' * 30)
for k, v in aluno.items():
    print(f' {k} é {v}', end=' ')
for e in aluno.keys():
    print(e)
print(aluno)