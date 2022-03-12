def aumentar(preco, taxa):
    calculo = preco + (preco * taxa / 100)
    return calculo


def dimunir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


valor = metade(200)
print(valor)
print(type(valor))