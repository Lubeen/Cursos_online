import random
al1 = input('Primeiro aluno :')
al2 = input('Segundo aluno :')
al3 = input('Terceiro aluno :')
al4 = input('Quarto aluno :')
lista = [al1, al2, al3, al4]
lista1 = [al1, al2, al3, al4]
random.shuffle(lista1)
print('A ordem para apresentação sera ')
print(lista1)

