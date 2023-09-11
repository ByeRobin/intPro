print("\nAct12")
n  = int(input("Ingresa el valor de n: "))
if n > 0:
    for i in range(1,n+1):
        print(i*n)

print("\nAct13")
m  = int(input("Ingresa el valor de m: "))
i = 0
sum = 0
while i < m:
    sum = sum + 1
    i = i + sum 
    if i > m:
        print(sum)

print("\nAct14")
#a 
n = int(input("Ingresa el valor de n: "))
if n > 0:
    for i in range(1,n+1):
        print(2*i)

#b 
n = int(input("Ingresa el valor de n: "))
if n > 0:
    for i in range(1,n+1):
        print((2*i)-1)
#c
n = int(input("Ingresa el valor de n: "))
if n > 0:
    for i in range(1,n+1):
        print(i**2)

#d
n = int(input("Ingresa el valor de n: "))
if n > 0:    
    for i in range(1,n+1):
        print((i**3) - (i**2))

#e
n = int(input("Ingresa el valor de n: "))
if n > 0:    
    for i in range(1,n+ 1) :
        print(1/(i**2))


print("\nAct15")
#a
n = int(input("Ingresa el valor de n: "))
sum = 0
for i in range(1,n+1):
    resultado = 2*i
    sum = sum + resultado
    print(sum)

#b
n = int(input("Ingresa el valor de n: "))

sum = 0
for i in range(1,n+1):
    resultado = 2**i 
    print("+",resultado)
    sum = sum + resultado
    print(sum)    
#c
n = int(input(" n = "))
sum = 0
for i in range(1,n+1):
    resultado = 3**i - 2**i
    sum = sum + resultado
    print(sum)

#d
n = int(input(" n = "))
sum = 0
for i in range(1,n+1):
    resultado = 1/(2**i)
    sum = sum + resultado
    print(sum)
#e) En el item anterior nos vamos hacercando al 1
