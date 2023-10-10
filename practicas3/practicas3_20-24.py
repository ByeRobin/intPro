print("\nAct20")

#a,b

m = 4
n = 6
for i in range(m,n+1):
    for j in range(m,n+1):
        print(i,j)

izquierda = int(input("n == "))
derecha = int(input("m == "))

stop = 0
n = izquierda 
left = izquierda
contador = 0

while stop < 1:
    print(left, n+contador)
    if n+contador < derecha:
        contador = contador + 1
    else:
        contador = 0
        left = left + 1
    if left == derecha and n + contador == derecha:
        stop = 1
        print(left,n + contador)

print("\nAct21")
#a

print("\Act22")
import random
ap = int(input("Ingresa el monto a apostar: "))
n = int(input("Ingresa tu numero (entre 0 y 99): "))

for i in range(0,1):
    numero_de_la_suerte = random.randint(0,99)
    print(numero_de_la_suerte)
    if numero_de_la_suerte == n:
        ganancias = ap*70
        print("Tus ganancias son de $",ganancias)
    else: 
        print("Segui participando")
