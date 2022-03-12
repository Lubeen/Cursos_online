print('descubra os triangulos')
a = int(input('Digite uma reta qualquer  '))
b = int(input('Digite outra reta qualquer  '))
c = int(input('Digite outra reta qualquer  '))
if a < b + c and b < a + c and c < a + b :
    print('Os numeros formam um Triangulo', end='')
    if a == b == c:
        print(' EQUILATERO')
    elif a != b != c != a:
        print(' ESCALENO')
    else:
        print(' ISOSCELES!')
else: print('Os numeros nao formam um triangulo')
