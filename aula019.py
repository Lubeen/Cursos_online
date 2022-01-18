'''dados = {'nome':'Luan','idade':23}
print(dados['idade'])
filme = {'titulo':'star wars','ano':1977,'diretor':'george lucas'

}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'o {k} é {v}')'''
'''pessoas = {'nome':'gustavo','sexo':'M','idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
del pessoas['sexo']
for k in pessoas.keys():
    print(k)
brasil = []
estado1 = {'uf':'Rio de janeiro','sigla':'RJ'}
estado2 = {'uf':'Sao paulo','sigla':'SP'}
brasil.append(estado2)
brasil.append(estado1)
print(brasil[0]['uf'])'''
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado'))
    brasil.append(estado.copy())
print()
'''for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')'''
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()