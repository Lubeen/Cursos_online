tupla = ('Arroz', 'feijao', 'Macarrao', 'Avestruz', 'licor',
         'limao', 'carne', 'bolo', 'milhao')
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
