# FUNCAO ANONIMA


anonima = lambda param: param + 2 
anonima_plus = lambda param1, param2: param1 + param2


# FUNCAO NORMAL
# X e Y vaO ser um parametro posicional

def soma_posional(x, y):
    """x e y são parametros posicionais.    """
    return x + y

# Com esse asterisco a funcao so pode ser chamada de maneira nomeada
def soma_explicitamente_nomeados(*, x=7, y=7):
    """ 
    X E Y são parametros nomeados.
    na falta de X E Y o valor 7 sera usado"""
    print(f'x: {x} e y:{y}')
    return x + y



# Com esse asterisco no meio o y é apenas nomeado e o x se torna posicional
def soma_explicitamente_nomeado_uma_variavel(x=7, *,  y=7):
    """ 
    X E Y são parametros nomeados.
    na falta de X E Y o valor 7 sera usado"""
    print(f'x: {x} e y:{y}')
    return x + y


    # Com esse traço tudo a esquerda precisa ser posicional
def soma_explicitamente_nomeados(x=7, y=7, /):
    """ 
    X E Y são parametros nomeados.
    na falta de X E Y o valor 7 sera usado"""
    print(f'x: {x} e y:{y}')
    return x + y


def soma_tudo_mix(x,y, /, z, *, w):
    return sum((x,y,z,w))