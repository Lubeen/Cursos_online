'''sexo  = ''
enquanto  sexo  ! =  'M'  ou  'F' :
    sexo  =  str ( input ( 'Digite seu sexo [M / F]:' )). superior (). tira ()
    print ( 'Dados invalidos, por favor tente novamente!' )
print ( 'Dados registrados com sucesso!' )'''
sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()
cont = 0
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor tente novamente!, por favor informe seu sexo!')).upper().strip()
    if sexo == 'M' or 'F':
        cont += 1
print('Dados registrados com sucesso!')
print(cont)
