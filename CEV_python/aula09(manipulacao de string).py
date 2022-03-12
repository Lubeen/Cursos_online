frase = 'Curso em Video Python  \n '
var = frase[9]
print(frase, var)
var1 = frase[9:13]
print(frase, var1)
var2 = frase[9:21]
print(frase, var2)
var3 = frase[9:21:2]
print(frase, var3)
var4 = frase[:5]
print(frase, var4)
var5 = frase[15:]
print(frase, var5)
var6 = frase[9::3]
print(frase, var6)

print(len(frase))
print(frase.count('o'))
print(frase.count('o,0,13'))
print(frase.find('deo'))
print('curso' in frase)
print(frase.replace('Python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
# frase.strip remove os espaços desnecessarios
# também tem a variacao r, para remover pela direita r.strip
# também tem a variacao l, para remover pela esquerda l.strip
print(frase.split())
print(''.join(frase))