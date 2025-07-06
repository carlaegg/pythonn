resultado=0
a=float(input("ingresa numero"))
b =float(input("ingresa numero"))
for i in range(abs(int(b))):
    resultado += a

if b<0:
    resultado = -resultado
print(resultado)