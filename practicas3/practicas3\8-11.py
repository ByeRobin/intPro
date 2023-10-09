print("\nAct8")
print("x(x+2)(x+3)")
i = int(input("Ingresa un valor entero de X: "))
if i**((i+2)*(i+3))== 1 and i**((i+2)*(i+3))!= -1:
        print(i," es solucion para esta ecuacion")
else:
    while i**((i+2)*(i+3)) != 1:
        resultado = i**((i+2)*(i+3))
        print("El resultado es:",round(resultado,3))
        print("No es solucion\n")
        i = int(input("Ingresa un valor entero de X: "))
        if i**((i+2)*(i+3))== 1 and i**((i+2)*(i+3))!= -1:
            print(i," es solucion para esta ecuacion")


print("\nAct9")
steps = 0
x = int(input("ingresa un valor x: "))
while x != 1 and x !=0:
    if x % 2 == 0:
        x = x/2
        steps = steps + 1
        print(int(x))
    elif x%2 != 0:
        x = 3*x + 1
        print(int(x))
        steps = steps + 1
print(f"\nEl programa repitio el proceso un total de: {steps} veces")


print("\nAct10")
#a
n = int(input("Ingresa un valor n: "))
i = 1
x = 1
while i < n:
    print(i)
    i = 2 ** x
    x = x + 1

#b
n = int(input("Ingresa un valor n: "))
if n < 0:
    print("El numero debe ser positivo.")
if n > 0:
    for i in range(0,n):
        print (2**i) 

#c
n = int(input("Ingresa un valor n: "))
if n < 0:
    print("El numero debe ser positivo.")
if n > 0:
    iteraciones = 1
    for i in range(0,n):
        i ** iteraciones
        iteraciones + 1

#c
n = int(input("Ingresa un valor n: "))
if n < 0:
    print("El numero debe ser positivo.")
if n > 0:
    iteraciones = 1
    i = 1
    for i in range(1,n+1):
        print(i ** iteraciones)
        iteraciones = iteraciones + 1
        i = i + 1


print("\nAct11")
#a
n = int(input("Ingresa un valor n: "))
if n > 0:
    for i in range(1,n+1):
        if n % i == 0:
            print(i,"Es divisor de ",n)

#b
n = int(input("Ingresa un valor n: "))
if n > 0:
    for i in range(1,n+1):
        if i % 2 == 0:
            if n % i == 0:
                print(i,"Es divisor de ",n)

#c
n = int(input("Ingresa un valor n: "))
if n > 0:
    iteraciones = 0
    for i in range (1,n+1):
        if n % i == 0:
            iteraciones = iteraciones + 1
    print(n, "tiene un total de ", iteraciones, "divisores")

#d 
n = int(input("Ingresa un valor n: "))
if n > 0:
    divisor = 0
    total_entre_div = 0
    for i in range (1,n+1):
        if n % i == 0:
            print(i,"Es divisor de ",n)
            divisor = i
            total_entre_div = divisor + i
    print("la suma total entre los divisores es:",total_entre_div)

#e
n = int(input("Ingresa un valor n: "))
c = int(input("Ingresa un valor c: "))

if n > 0 and c > 0 and n > c:
    medidor_de_divisores = 0
    for i in range(1,n):
        if n % i == 0:
            medidor_de_divisores = medidor_de_divisores + 1
            print(i,"Es divisor de ",n)
            if medidor_de_divisores == c:
                break

#f

n = int(input("Ingresa un valor n: "))
c = int(input("Ingresala cuantos ultimos divisores de n mostrar: "))

i = n
contador = 0
stop = 0
while i <= n:
    if n % i == 0:
        stop = stop + 1
        print(i,"es divisor de",n)
        if stop >= c: 
            i = n + 1
        else: i = i - 1
    else: i = i - 1
