def contador(i, f, p):
    print(f'Contagem de {i} a {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
        print('FIM!')


# Codigo principal
contador(1, 10, 1)






