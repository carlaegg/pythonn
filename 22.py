fibonacci = [0, 1]
while True:
    siguiente = fibonacci[-1] + fibonacci[-2]
    if siguiente > 100:
        break
    fibonacci.append(siguiente)
print("a) Términos generados:", fibonacci)
pares = [num for num in fibonacci if num % 2 == 0]
print("b) Cantidad de términos pares:", len(pares))
print("c) ¿El 50 está en la serie?", "Sí" if 50 in fibonacci else "No")