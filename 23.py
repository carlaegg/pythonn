hombres_mas35=0
mujeres_may30=0
cantidad=int(input("ingrese cuantas personas compiten"))
for i in range(cantidad):
    edad=int(input("ingrese edad"))
    sexo=input("ingrese el sexo M masculino o F femenino")
    tiempo=float(input("ingrese tiempo"))
    if sexo=="M":
        if edad>=35:
            hombres_mas35 +=1
            if 40<=tiempo<=60:
                print ("clasifica")
            else:
                print("no clasifica")
        else:
            print("no clasifica")        
    if sexo=="F":
        if edad>30:
            mujeres_may30 +=1
            if  40<=tiempo <=80:
                print("clasifica")
            else:
                print("no clasifica")
        else:
            print("no clasifica")