suma = 0
for numero in range(1, 101): 
    if numero % 10 != 5:  
        suma += numero

print("La suma de los números del 1 al 100 que no terminan en 5 es:", suma)
