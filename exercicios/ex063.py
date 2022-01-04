print('SEQUENCIA DE FIBONACCI')
termo = int(input('Digite quantos termos voce quer '))
t1 = 0
t2 = 1
cont = 3
mais = 1
total = termo
print('{} -> {}'.format(t1, t2), end=' ')
while mais != 0:
    total = total + mais
    while cont <= total:
        t3 = t1 + t2
        print('-> {}'.format(t3), end=' ')
        t1 = t2
        t2 = t3
        cont += 1
    mais = int(input('Digite quantos termos a mais voce quer ver :'))
print('Fim')
