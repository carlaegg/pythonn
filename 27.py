numeros=[]
numeros_dobles=[]

for i in range(30):
    num=int(input("ingrese un numero: "))
    numeros.append(num)
    if num== (numeros[i-1]*2):
        numeros_dobles.append(num)

print(numeros_dobles)

