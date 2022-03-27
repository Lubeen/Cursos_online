def calculo_medidas(*num):
    lista = []
    for c in range(1,7):
        medidas = float(input('Digite um número :'))
        lista.append(medidas)    
    dam = lista[0] / 10
    hm = lista[1] / 100
    km = lista[2] / 1000
    dm = lista[3] * 10
    cm = lista[4] * 100
    mm = lista[5] * 1000
    return {'dam':dam, 'hm':hm, 'km':km, 'dm':dm, 'cm':cm, 'mm':mm}


print(calculo_medidas())

