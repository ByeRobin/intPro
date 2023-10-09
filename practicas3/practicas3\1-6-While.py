print("\nAct 1")
#a
i = 1
while i <= 5 :
    print(i)
    i = 1 + i

#b
i = 1
num = int(input("ingresa un numero  natural: "))
while i <= num :
    print(i)
    i = 1 + i

print("\nAct2")
#a
i = 4
while i <= 7 :
    print(i)
    i = 1 + i

#b
m = int(input("ingresa un valor natural M: ")) 
n = int(input("Ingresa un valor natural N: "))

while m>=n:
    print()

print("\nAct3")
#a
i = 10
while i < 10 + 5:
    i = i + 1
    print(i)

#b
n = int(input("Ingrese un numero natural: "))
count = 0
while count < 5:
    count = count+ 1
    print(n + count)

#c
n = int(input("Ingrese un numero natural: "))
c = int(input("Ingrese un numero natural: "))

count = 0
while count < c:
    count = count+ 1
    print(n+count)


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
i = 8
print(i)
while i!=3:
    i = i -1
    print(i)

print("\nAct6")

i = 15
print(i)
while i!=6:
    i = i -3
    print(i)
