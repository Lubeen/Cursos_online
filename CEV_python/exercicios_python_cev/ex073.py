classificacao = ('Atletico-MG', 'Flamengo', 'Palmeiras',
                 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense'
                 , 'America-MG', 'Atletico-GO', 'Santos', 'Ceara SC',
                 'Internacional', 'Sao paulo', 'Atletico-PR', 'Cuiaba', 'Juventude',
                 'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os cinco primeiros são {classificacao[0:5]}')
print(f'Os ultimos 4 colocados são {classificacao[-4:]}')
print(f'Os times em ordem alfabetica são {sorted(classificacao)}')
print(f'O time da chapecoense esta na posicao {classificacao.index("Chapecoense")+1}')



