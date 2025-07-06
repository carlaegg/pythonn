
def clasificar_poligono(lados):
    match lados:
        case 3:
            return "Triángulo"
        case 4:
            return "Cuadrilátero"
        case 5:
            return "Pentágono"
        case _:
            return "No es un triángulo, cuadrilátero ni pentágono"
        
lados=int(input("ingrese numero de lados"))
print(clasificar_poligono(lados))