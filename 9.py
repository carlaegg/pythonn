cont=0
prom=0
sumador=0
while cont<15:
    numero=int(input("ingrese numeros"))
    sumador=sumador+numero
    cont+=1

prom=sumador/cont
print("el promedio es de ",prom)