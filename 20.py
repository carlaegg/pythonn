
numero1=float(input("ingrese el primer numero: "))
mayor=numero1
menor=numero1

for i in range (1,100):
    numero=float(input("ingrese numero: "))
    if numero > mayor:
        mayor=numero
        
    elif numero<menor:
        menor=numero
print("mayor es: ",mayor)
print("menor es: ",menor)