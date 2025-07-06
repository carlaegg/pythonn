cont=0
negativos=0
positivos=0
nulos=0
while cont<4:
    numero=float(input("ingrese numero\n"))
    if numero==0:
     nulos=nulos+1
    elif numero>0:
     positivos=positivos+1
    else:
       negativos=negativos+1
    cont+=1

print("los positivos son",positivos,"\n","los negativos son",negativos,"\n","los nulos son",nulos)