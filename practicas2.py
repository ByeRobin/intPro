#Ejercicio 1 
print('\nAct1')
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese un numero entero: "))
c = int(input("Ingrese un numero entero: "))
print("Usted ingresó los valores:", a, b, c)

if a > b:
    print(a, "es mayor que", b)
if a == b:
    print(a, "y", b, "son iguales")
if a > b and a > c:
    print(a, "es el mayor de todos")
if b < a and b < c:
    print(b, "es el menor de todos")
if a > b or a > b:
    print(a, "es mayor que alguno de los otros dos")
if a <= b or a <= b:
    print(a, "es menor o igual que alguno de los otros dos")
if a == b and a == c and c == b:
    print("Los tres numeros son iguales")
if a != b and a != c and c != b:
    print("Los tres numeros son distintos")
if a % 2 == 0:
    print(a, "es par")
if a % 2 == 0 or c % 2 == 0 or b % 2 == 0:
    print("alguno es par")
if a % 2 != 0 and c % 2 != 0 and b % 2 != 0:
    print("ninguno es par")
if a % 2 == 0 and c % 2 == 0 and b % 2 == 0:
    print("todos son pares")
if a % 3 == 0:
    print(a, "es multiplo de 3")
if a % 3 == 0 and a % 5 == 0:
    print(a, "es multiplo de 3 y de 5")
if  a % 3 == 0 and a % 2 == 0:
    print(a, "es multiplo de 3 y par")
if a - b > 0:
    print(a, "-", b, "da un numero positivo")
if a - b > 0 and (a - b) % 2 == 0:
    print(a, "-", b, "da un numero par positivo")

#Ejercicio 2
print('\nAct2')
edad = int(input('Ingrese su edad: '))
distancia = int(input('Ingrese la distancia entre su vivienda y el lugar de votacion (reflejada en km): '))

if edad >= 18 and edad <= 70 and distancia <= 500:
    print('Usted tiene que ir a votar')
else:
    print('Usted no tiene que ir a votar')

#Ejercicio 3
print('\nAct3')
print('Codigo a: Su print sera "perro"')
print('Codigo b: Su print sera "Manzana"')
print('Codigo c: SU print sera "Te quiero" seguido por "bien lejos')
print('Codigo d: Su print sera "Hola"')
print('Codigo e: "p1 y p2 no son iguales!"')
print('Codigo f: "Python es muy sensible!"')

#Ejercicio 4
print("\nAct4")
print('El valor de a que imprime "hola!" es unicamente 0, cualquier otro valor imprimira "chau!"')

#Ejercicio 5
print("\naAct5")
nota = int(input('Escribe el valor de tu calificacion: '))
if nota < 4:
    print('Debe recuperar')

#Ejercicio 6
print("\nAct6\na)")
a = int(input('Ingresa un nummero: '))
b  = int(input('Ingresa un nummero: '))
if a > b:
    print(f'{a} es mayor que {b}')
elif b > a:
    print(f' {b} es mayor que {a}')
elif a == b:
    print(f'{a} y {b} son iguales')

print('"\nAct6\nb)')
a = int(input('Ingresa un nummero: '))
b  = int(input('Ingresa un nummero: '))
if a < b:
    print(f'{a} es menor que {b}')
elif b < a:
    print(f' {b} es menor que {a}')
elif a == b:
    print(f'{a} y {b} son iguales')

#Ejercicio 7
print("\nAct7")
a = float(input('Ingresa el valor flotante: '))
b = float(input('Ingresa el valor flotante: '))
promedio = (a + b)/ 2
print(f"el promedio entre {a} y {b} es {promedio}")
if promedio > 7:
    print("Cumples los requisitos para promocionar")
else: 
    print("No cumples los requisitos, deberas recursar")

#Ejercicio 8 
print("\nAct8")
num = int(input('Ingresa un numero positivo: '))
if num <= 0:
    print('El numero debe ser positivo')
elif num > 0 and num < 9:
    print('Tiene una sola cifra')
else: print('Tiene 2 o mas cifras')

#Ejercicio 9 
print("\nAct9")
lista_dni = [30612453,23763290,21448503,34582048,15364857]
dni_ingresado = int(input("Ingresa el dni: "))
if dni_ingresado not in lista_dni:
    print("El dni ingresado no essta en nuestra base de datos")
else : print("El dni existe en la lista")

#Ejercicio 10
print("\nAct10")
kw = int(input("Ingrese la cantidad de KW que indica el medidor: "))
tarifa_fija = 480
precio_por_kw = 25.5
impuestos = 78

if kw <= 200 and kw > 0:
    print(f"Consumiste {kw} kw y estan incluidos en la tarifa estandar\nEl monto total a pagar sera de ${tarifa_fija}")
elif kw >= 200:
    monto_final = (kw - 200 * 25.5) + 78
    print(f"Consumiste {kw} kw, por tanto exediste la tarifa estandar\nEl monto total a pagar sera de ${monto_final}")
else: print('Ingrese un valor valido')

#Ejercicio 11
print("\nAct11")
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))
c = int(input("Ingresa un numero: "))

if a > b and a > c:
    print(f"{a} es el mayor de todos") 
elif b > a and b > c:
    print(f"{b} es el mayor de todos") 
elif c > b and c > a:
    print(f"{c} es el mayor de todos") 

#Ejercicio 12
print("\nAct12")
nota = int(input("Ingresa la nota: "))
if nota <= 3 and nota > 0:
    print("No alcanzas nuesto paramtero de promocion, estas desaprobado")
elif nota > 3 and nota <= 6:
    print ("No alcanzaste nuestro parametro de promocion pero estas en condiciones de rendir une examen final")
elif nota > 6 and nota <= 10:
    print("Alcanzaste nuestro parametro de promocion")
else: print("Ingresa un valor valido")

#Ejercicio 13
print("\nAct13")
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{b} es mayor que {a}")

#Ejercicio 14
print("\nAct14")
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))
if a < b:
    a_new = b
    b_new = a
    print(f"{b_new} es mayor que {a_new}")
elif a > b:
    print(f"{a} es mayor que {b}")
