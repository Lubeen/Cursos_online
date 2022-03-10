'''Elabore um app que leia 3 valores inteiros e apresente na tela o maior e o menor deles.'''


def maior_menor(*n):
    for p in range(1, 4):
        valor = int(input('Digite um numero inteiro: '))
        lista.append(valor)
    return lista


# Programa principal
lista = []
resultado = maior_menor(lista)
print(f'O maior numero inteiro foi de {max(resultado)} e o menor valor foi de {min(resultado)}')




