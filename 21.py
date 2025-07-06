mayor_18=[]
menores_12=0
entre10_16=0
sum=0
edad=float(input("ingrese edad: "))
nombre=str("ingrese nombre: ")
if edad>18:
    mayor_18.append(nombre)
mayor=edad
menor=edad

for i in range (1,50):
    numero=float(input("ingrese edad: "))
    if edad> mayor:
        mayor=edad
        
    elif numero<menor:
        menor=numero
print("mayor es: ",mayor)
print("menor es: ",menor)