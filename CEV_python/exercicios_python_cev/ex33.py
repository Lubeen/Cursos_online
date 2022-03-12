a = int(input('Digite um  numero qualquer: '))
b = int(input('Digite outro número qualquer: '))
c = int(input('Digite o ultimo numero qualquer'))
menor = a
if a < b and a < c :
    menor = a
if b < a and b < c :
    menor = b
if c < a and c < b :
    menor = c
print('O menor número digitado foi {}'.format(menor))
maior = a
if a > b and a > c :
    maior = a
if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
print('O maior numero digitado foi:{} '.format(maior))
