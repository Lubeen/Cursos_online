import random
print('Sorteio de aluno para apagar o quadro')
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print('O escolhido para apagar foi {}'.format(escolhido))
print(type(escolhido))
