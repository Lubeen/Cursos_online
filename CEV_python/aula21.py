''' Interactive Help
Docstrings
Argumentos ou parametros opcionais
Escopo de varivaies
Retorno de resultados
'''
# Interactive Help*
# help()
# print(input.__doc__)

# Docstrings*

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')

help(contador)

# Parametros opcionais*


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()


# Escopo de variaveis


def teste(b):
    # x é uma variavel local
    # especificar a variavel global
    global a
    a = 8
    b += 4
    c = 2
    x = 8
    print(f'Na funcao teste n vale {n}')
    print(f'Na funcao teste, x vale {x}')
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa principal
# n é uma variavel global
n = 2
print(f'No programa principal, n vale {n}')
a = 5
teste(a)
print(f'No programa principal, a vale {a}')


# Retorno de Valores
# RETURN


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus calculos deram {r1}, {r2} e {r3}')
