cont=0
negativos=[]
positivos=0
nulos=0
acumulador=0
contpositivos=0
while cont<75:
    numero=float(input("ingrese numero: \n"))
    if numero==0:
     nulos+=1
    elif numero>0:
     positivos+=numero
     contpositivos+=1
    else:
       negativos.append(numero)
    cont+=1

promedio=positivos/contpositivos if contpositivos > 0 else 0
print("el promedio de positivos es",promedio,"\n","los negativos son",negativos,"\n","la cantidad de nulos es",nulos)