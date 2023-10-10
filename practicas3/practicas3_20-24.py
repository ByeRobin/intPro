print("\nAct20")

#a,b

m = 4
n = 6
for i in range(m,n+1):
    for j in range(m,n+1):
        print(i,j)

izquierda = int(input("n == "))
derecha = int(input("m == "))
der = n
i = 0
cont = 0

while i < 1:
    print(n,der+cont)
    if  der + cont < m:
        cont += 1
    else:
        cont = 0
        n += 1
    if n == m and der + cont == m:
        i = 3
        print(n,der+cont)

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
