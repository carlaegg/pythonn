i=0

while i==0:
    A = int(input('Ingrese un número: '))
    B = int(input('Ingrese un número: '))
    C = int(input('Ingrese un número: '))
    D = int(input('Ingrese un número: '))

    if A//10 == 0 and B//10 == 0 and C//10 == 0 and D//10 == 0:
        i=1
    else:
        print('Números erróneos, ingresar nuevamente! \n')     

A = A*1000
B = B*100
C = C*10
total = A+B+C+D
print('El número resultante es igual a ', total)