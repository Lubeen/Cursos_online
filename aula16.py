#lanche = () = tupla, [] = lista, {} = dicionario
# tuplas sao imutaveis
# lanche[1] = refrigerante
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Vou comer {comida}')
print('Comi pra caramba!')
for comida in range(0, len(lanche)):
    print(f'Vou comer {lanche[comida]} na posicao {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Acabei')
print(sorted(lanche))
a = (0, 2, 4, 6, 8, 10)
b = (1, 3, 5, 7, 9)
c = a + b
print(c.index(8))
# a ordem importa para somar tuplas e tuplas
# index é para mostrar em qual posicao esta
pessoa = ('Luan', 22, 'M', 62)
print(pessoa)
# tuplas podem ter varios tipos de dados
# voce nao pode mudar as tuplas, mas pode apagar a tupla e sobrescrever
pessoa = ('camila', 24, 'F')
print(pessoa)
del (pessoa)

