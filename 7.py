cont=0
negativos=0
positivos=0
while cont<100:
    numero=float(input("ingrese numero\n"))
    if numero>0:
       positivos=positivos+numero
    else:
       negativos=negativos+numero
    cont+=1

print("los positivos son",positivos,"\n","los negativos son",negativos)