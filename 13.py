Mayores_60=0
Menores_20=0
Entre_55_85=0
n=int(input("ingrese cuantos numeros va a trabajar: "))
for i in range(n):
    numero=float(input("ingrese numero: "))
    if numero>60:
       Mayores_60+=1
    if numero<20:
     Menores_20+=1
    if numero<=55 and numero <=85:
       Entre_55_85+=1
print("los mayores a 60 son: ",Mayores_60,"\n los que estan entre 55 y 85 son",Entre_55_85,"\n los menores a 20 son",Menores_20)

