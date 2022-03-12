primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA :'))
cont = 1
mais = 10
total = 0
termo = primeiro
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Voce quer ver quantos termos a mais? '))
print('progressão finalizada com {} termos mostrados '.format(total))
