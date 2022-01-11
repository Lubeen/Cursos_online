'''dados = list()
dados.append('Luben')
dados.append(dados[:])
print(dados)
pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
teste = list()
teste.append('Luben')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Luan'
teste[1] = 23
galera.append(teste[:])
print(galera)
print(teste)'''
'''teste = []
teste.append('Luan')
teste.append(22)
galera = []
galera.append(teste[:])
teste[0] = 'Joao'
teste[1] = 40
galera.append(teste[:])
print(galera)'''
'''galera = [['felipe', 19], ['Ana', 33], ['joaquim', 13], ['Maria', 45]]
print(galera[0][0])
for p in galera:
    print(p)'''
galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
print(galera)