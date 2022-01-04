lista = ['pizza', 'suco', 'arroz', 'cachorro quente', 'Macarronada']
print(lista)
lista.append('Licor')
print(lista)
lista.insert(0, 'cerveja')
print(lista)
del lista[2]
print(lista)
lista.pop(1)
print(lista)
lista.remove('Licor')
print(lista)
if 'pizza' in lista:
    lista.remove('pizza')
print(lista)
valores = list(range(4,11))
print(valores)
valores = [2,5,8,1,7,9,8,9,7,1,]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei {v}')
# Quando voce iguala uma lista na outra, acontece uma ligação entre elas ex
lista2 = lista
print(lista)
print(lista2)
lista2[2] = 'Feijao'
print(lista)
print(lista2)
# para criar uma copia é assim
lista2 = lista[:]
print(lista)
print(lista2)
lista2[3] = 'Lapis'
print(lista)
print(lista2)