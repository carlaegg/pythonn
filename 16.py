contador=0
primaria=[]
secundaria=[]
universidad=[]
while contador<100:
    nombre =input("ingrese nombre: ")
    edad=int(input("ingrese edad: "))

    if edad>=6 and edad <=12:
       primaria.append(nombre)       

    if edad >=13 and edad<=17:
        secundaria.append(nombre)
    if edad>17 :
        universidad.append(nombre)
    contador +=1

print("primaria",primaria)
print("secundaria", secundaria)
print("universidad",universidad)
    