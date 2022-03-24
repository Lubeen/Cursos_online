def soma(n1, n2):
   resp = n1 + n2
   return resp


# Programa principal
n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número inteiro:'))
resultado = soma(n1,n2)
print(f'{n1} + {n2} = {resultado}')