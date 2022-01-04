medidas = float(input('Digite um número :'))
dam = medidas / 10
hm = medidas / 100
km = medidas / 1000
dm = medidas * 10
cm = medidas * 100
mm = medidas * 1000
print('Seu número em metros é {} \n'.format(medidas))
print('além disso em dam é {:.0f} em hm é {:.0f} em km é {:.0f} em dm é {:.0f} em cm é {:.0f} e em mm é {:.0f}'.format(dam,hm,km,dm,cm,mm))
