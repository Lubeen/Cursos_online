'''def mostraLinha():
    print('-------------------------------------------')


# programa principal
mostraLinha()
print('       Sistema de Alunos           ')
mostraLinha()
mostraLinha()
print('       Cadastro de Funcionarios        ')
mostraLinha()
mostraLinha()
print('       Erro do Sistema         ')
mostraLinha()'''
'''def mensagem(msg):
    print('--------------------------------------------')
    print(msg)
    print('--------------------------------------------')
    mensagem('Sistema de alunos')'''
'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa principal
titulo('    Curso em Video  ')
titulo('    Aprenda Python  ')
titulo('    Gustavo Guanabara   ')'''

'''def soma(a, b):
    s = a + b
    print(s)


#Programa principal
soma(5, 6)
soma(10, 30)
soma(b=11, a=23)'''

'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')


# programa principal
contador(2, 1, 7) 
contador(8, 0)
contador(4, 4, 7, 6, 2)'''
'''def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
#Listas 
# Programa principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)'''

# Desempacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f' somando os valores {valores} temos {s}')


# Programa principal
soma(5, 2)
soma(2, 9, 4)