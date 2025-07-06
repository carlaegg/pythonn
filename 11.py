pares=0
impares=0
cont=0
while cont<75:
        numero=float(input("ingrese numero: \n"))
        if   numero%2 ==0:
          pares+=numero
     
        else:
         impares+=numero
     
        cont += 1

print("suma de pares es: ",pares,"suma de impares es: ",impares)
