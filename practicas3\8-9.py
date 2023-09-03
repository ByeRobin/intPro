x = int(input("Ingresa un valor entero de X: "))
if x**((x+2)*(x+3))== 1:
    print (True)
else: print(x**(x+2)*(x+3))


print("x(x+2)(x+3) = 1")
i = 0
resultado = i**((i+2)*(i+3))
while resultado != 1:
    i = int(input("Ingresa un valor entero de X: "))
    resultado = i**((i+2)*(i+3))
    print(f"{i} no puede ser solucion a esta ecuacion \n{resultado} es diferente a 1")
