nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome maiusculo é : ', nome.upper())
print('Seu nome minusculo é :', nome.lower())
print('a quantidade de letras sem espaços é : ', len(nome)-nome.count(' '))
spl = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(spl[0])))

