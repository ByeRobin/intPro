print("\nAct8")
print("x(x+2)(x+3)")
i = int(input("Ingresa un valor entero de X: "))
if i**((i+2)*(i+3))== 1:
        print(i," es solucion para esta ecuacion")
else:
    while i**((i+2)*(i+3)) != 1:
        resultado = i**((i+2)*(i+3))
        print("El resultado es:",round(resultado,3))
        print("No es solucion\n")
        i = int(input("Ingresa un valor entero de X: "))
        if i**((i+2)*(i+3)) == 1:
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

