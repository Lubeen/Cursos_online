lista = list()
for c in range(0, 5):
    num = int(input('Digite um valor qualquer'))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f'os valores digitados em ordem foram {lista}')
# lucas vai programar muito!
# Anderson o cara
