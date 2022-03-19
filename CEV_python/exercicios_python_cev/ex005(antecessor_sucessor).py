#  Antecessor e Sucessor

def antecessor_sucessor(n1, n2):
    print(f'o numero digitado é {n1} e o antecessor dele é {n1 - 1} e o sucessor dele é {n1 + 1}')
    print(f'o numero digitado é {n2} o antecessor dele é {n2 - 1} e o sucessor dele é {n2 + 1}')


# Programa principal
n1 = int(input('digite um numero'))
n2 = int(input('Digite outro numero'))
antecessor_sucessor(n1,n2)