# Des | empacotamento de argumentos

# Nessa funcao, o metodo *args recebe tudo menos parametros nomeados
# O X e Y recebem nomeados ou posicionados

def sum(x, y, *args):
    print(args)
    print(type(args))
    return x, y, sum(args)


# Porém com o parametro ** podemos ter os nomeados
def sum(*grupo_posicional, **grupo_nomeado):
    """EMPACOTAMENTO."""
    print(grupo_posicional, grupo_nomeado)
    print(type(grupo_posicional), type(grupo_nomeado))
    return  grupo_posicional, grupo_nomeado

# DICA SE FOR USAR GRUPOS NÃO USAR ESSAS FLAGS NOVAS

lista = [-1, 2, 3, 4, -10]

# Roda no terminal isso meu_min(*lista)

def meu_mim(a,b,c,d, *args):
    return min((a,b,c,d, *args))


dicionario = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

def meu_max(a=0, b=0, c=0,d=0):
    return max((a,b,c,d))


# Roda no terminal isso meu_max(**dicionario)


l = [1,2,3]
d = {
    'd':4,
    'e':5
}

def meu_mix(a,b,c, d=0, e=0):
    return a,b,c,d,e

# Roda no terminal isso meu_mix(*l, **d)