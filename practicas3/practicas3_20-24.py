print("\nAct20")

#a,b

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
m = int(input("ingresa el valor de m: "))
n = int(input("ingresa el valor de n: "))
left1 = m
left2 = left1

i = 0
while i < 1:
    print(left1,left2)
    if left2 < n and left2 >= left1:
        left2 += 1
    
    else:
        left1 += 1
        left2 = left1
    if left1 == n and left2 == n:
        print(left1,left2)
        i = 1

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


import random

print("\Act23")

print("\nJuguemos piedra papel o tijeras\n")
x = input("Que juegas? (piedra/papel/tijeras): ")

if x == 'papel':
    y = random.randint(1,3)
    print(y)
    if y == 1:
        print('Ganaste, elegi piedra')
    if y == 2:
        print('Empate, elegi papel tambien')
    if y == 3:
        print("perdiste, elegi tijeras")
if x == 'tijeras':
    y=random.randint(1,3)
    print(y)
    if y == 1:
        print('Perdiste, elegi piedra')
    if y == 2:
        print('Ganaste, elegi papel ')
    if y == 3:
        print("Empate elegi tijeras tambien")
if x == 'piedra':
    y=random.randint(1,3)
    print(y)
    if y == 1:
        print('Empate, elegi piedra tambien')
    if y == 2:
        print('Perdiste, elegi papel')
    if y == 3:
        print("Ganaste, elegi tijeras")


#No comprendo la Act24
