for i in range(0,100):
    nombre_producto=input("nombre del producto: \n")
    cantidad=int(input("cantidad del producto: \n"))
    if cantidad<100:
        faltante=abs(cantidad-100)
        print("ingrese los datos del proveedor de",nombre_producto, "faltan",faltante)