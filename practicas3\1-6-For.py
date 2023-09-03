print("\nAct1")
#a
for i in range(1,5+1):
    print(i)
#b
n = int(input("Ingresa un valor numerico: "))
if n > 0:
    for n in range(1,n+1):
        print(n)
else: print("Utiliza un numero natural")


print("\nAct2")
#a
for i in range(4,7+1):
    print(i)

#b
m = int(input("ingresa un numero  natural: ")) #5
n = int(input("ingresa un numero  natural: ")) #10

if m!= n and m < n:
    for i in range(m,n+1):
        print(i)

if m!= n and m > n:
    for i in range(n,m + 1):
        print(i)


print("\nAct3")
#a
for i in range(10,15+1):
    print(i)

#b
n = int(input("Ingresa el valor: "))
for i in range(n,n+6):
    print(i)

#c
n = int(input("Ingresa el valor n: "))
c = int(input("Ingresa el valor c: "))

if c >= 0:
    for i in range(n,n+c+1):
        print(i)
else: print("El valor de c debe ser positivo")


print("\nAct4")
#a
for i in range(5,11+1,2):
    print(i)

#b
m = int(input("ingresa un numero  natural: ")) 
n = int(input("ingresa un numero  natural: "))

for i in range(m,n+1,3):
    print(i)

#c
n = int(input("ingresa un numero N natural: ")) 
m = int(input("ingresa un numero M natural: "))
p = int(input("ingresa un numero P natural: ")) 

if m!= n and m < n:
    for i in range(m,n+1,p):
        print(i)

if m!= n and m > n:
    for i in range(n,m+1,p):
        print(i)
