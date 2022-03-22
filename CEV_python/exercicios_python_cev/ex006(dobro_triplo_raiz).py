# Dobro, Triplo, Raiz Quadrada

def dobro_triplo_raiz(num):
    dobro = num * 2
    triplo = num * 3
    raiz = num**(1/2)
    return dobro, triplo, raiz


# Programa principal
num = int(input('Digite um numero:'))
res = dobro_triplo_raiz(num)
resultado = []
resultado = res
print(f'O número digito foi {num}, o dobro  é {resultado[0]} o triplo é {resultado[1]} e a raiz quadrada é {resultado[2]}')