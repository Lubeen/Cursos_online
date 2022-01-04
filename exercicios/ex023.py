'''num = int(input('Digite um numero entre 0 e 9999 : '))
n = str(num)
print('Vamos analisar o numero {}'.format(num))
print('A dezena é {}'.format(n[1]))
print('A unidade é {}'.format(n[0]))
print('A centena é {}'.format(n[2]))
print('A milhar é {}'.format(n[3]))'''
num = int(input('Digite um numero de 0 a 9999 :'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('a unidade é', u)
print('a dezena é', d)
print('a centena é', c)
print('o milhar  é', m)