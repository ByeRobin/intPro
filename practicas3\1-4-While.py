print("\nAct4")
#a
i = 5
print(i)
while i!=11:
    i = i + 2
    print(i)

#b
m = int(input("ingresa un valor natural M: ")) 
n = int(input("Ingresa un valor natural N: "))
if  m!= n:
    if m < n:
        i = m
        print(i)
        while i<n:
            i = i + 3
            print(i)

    if n < m:
        i = n
        print(i)
        while i<m:
            i = i + 3
            print(i)

#c
n = int(input("ingresa un numero N natural: ")) 
m = int(input("ingresa un numero M natural: "))
p = int(input("ingresa un numero P natural: ")) 

if  m!= n:
    if m < n:
        i = m
        print(i)
        while i<n:
            i = i + p
            print(i)

    if n < m:
        i = n
        print(i)
        while i<m:
            i = i + p
            print(i)

print("\nAct5")
