print("\nAct1")
#a
for n in range(1,5+1):
    print(n)
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

if m!= n and m > n:
    for i in range(m,n+1):
        print(i)

elif m!= n and n > m:
    for i in range(n,m + 1):
        print(i)

else: print("se ejecuto el else")

