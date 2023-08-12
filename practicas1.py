#Ejercicio 6
print('Mi primer programa en python')

#Ejercicio 7
print('v\n \ne \n \nr \n \nt \n \ni \n \nc \n \na \n \nl')

#Ejercicio 8
print('*****\n*   *\n*   *\n*   *\n*****')

#Ejercicio 9 
print('*\n***\n*****\n*******\n*********')

#Ejercicio 10
dato = input('Dame un dato: ')
print(dato)

#Ejercicio 11
valor  = input()
print(f"******************************\n El resultado es: {valor}\n *****************************")

#Ejercicio 12:

#ejercicio 2 

#def fraccionMasUno(x,y):
#    return x/y + 1

x = float(input('x = '))
y = float(input('y = '))
resultado = x/y + 1
print(resultado)

#def fraccionSumRes(x,y):
#    return x+y/x-y

x = float(input('x = '))
y = float(input('y = '))
resultado = x+y/x-y
print(resultado)

#def fraccionSobreFraccion(x,y,z):
#    return (x + y/z) / (x -y/z)

x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))
resultado = (x + y/z) / (x -y/z)
print(resultado)

#def corchetesYparentesis(x,y):
#    return ((x+y)**2)**2

x = float(input('x = '))
y = float(input('y = '))
resultado = ((x+y)**2)**2
print(resultado)

#Ejercicio 3
x = float(input('x = '))
y = float(input('y = '))
resultado = x + y
print(resultado)

#Ejercicio 4
float(input('tu valor elegido es: '))
y = x + 1 
print(y)

#Ejercicio 5
x = float(input('x = '))
z = float(input('z = '))
y = x + z /2
print(y)

#Ejercicio 13
montoinicial = float(input('Ingresa la cantidad que deseas ingresar: '))
meses = float(input('Ingresa el plazo de disposicion(en meses): '))
incremento = (montoinicial * 6/100) * meses
monto_a_devolver = montoinicial + incremento
print(f'Al finalizar tu plazo, el incremento el total a devolver sera de: {monto_a_devolver}')

#Ejercico 14

llamadas_totales = float(input("Ingresa el total de llamadas realizadas: "))
minutos = float(input("ingresa la cantidad de minutos utilizados: "))

NombreDelUsuario = {
    "Total de llamadas", llamadas_totales,
    "cantidad de minutos", minutos,
}

costo_final = (1.5 * minutos) + llamadas_totales * 12
print(f"El costo total es: {costo_final}")

#Ejercicio 15

sueldo_base = 42000

venta1 = int(input("De cuanto fue tu primera venta: "))
venta2 = int(input("De cuanto fue tu segunda venta: "))
venta3 = int(input("De cuanto fue tu tercera venta: "))

saldo_final = sueldo_base + venta1 *10 /100 + venta2 *10 /100 + venta3 * 10 /100
print(saldo_final)

#Ejercicio 16
segundos_del_dia = 24*60*60
segundos_de_una_hora = 60*60
print(f"Una hora tiene {segundos_de_una_hora} segundos, y un dia {segundos_del_dia}.")

segundos_para_calcular = int(input("Ingrese una cantidad de segundos: "))
segundos_a_minutos = print(round(segundos_para_calcular / 60)) 
segundos_a_horas = print(round(segundos_para_calcular/60/60))
segundos_a_dias = print(round(segundos_para_calcular/60/60/24))

#Ejercicio 17

lista_de_billetes = [100,200,500,1000]
retiro = int(input("(Si el valor del monto es menor a 100 no se podra retirar)\nIngresa el monto a retirar: "))

#Cuantos de 1000
billetes_1000 = retiro // 1000
print(f"El cajero soltara {billetes_1000} billetes de 1000")

#Cuanto sobra
resto_de_billetes = retiro % 1000
print(resto_de_billetes)

#Cuantos de 500
billetes_de_500 = resto_de_billetes // 500
print(f"El cajero soltara {billetes_de_500} billetes de 500")

#Cuanto sobra
resto_de_billetes2 = resto_de_billetes % 500
print(resto_de_billetes2)

#Conseguir cuantos de 200
billetes_de_200 = resto_de_billetes2 // 200
print(f"El cajero soltara {billetes_de_200} billetes de 200")

#Cuanto sobra
resto_de_billetes3 = resto_de_billetes2 % 200
print(resto_de_billetes3)

#Cuantos de 100
billetes_de_100 = resto_de_billetes3 // 100
print(f"El cajero soltara {billetes_de_100} billetes de 100")

#Cuanto sobra
resto_de_billetes4 = resto_de_billetes3 % 100
print(billetes_de_100)

#Ejercicio 18

segundos = int(input('Ingresa la cantidad de segundos: '))
minutos = round(segundos / 60)
horas = round(minutos / 60)
dias = round(horas/24)

print(f'{segundos} segundos son: {minutos},{horas} y {dias}')

#Ejercicio 19

primeraVariable = input('Ingresa el valor de x: ')
segundaVariable = input('Ingresa el valor de y: ')

x == segundaVariable
y == primeraVariable

print(f'El valor de x es: {x}')
print(f'El valor de y es: {y}')

#Ejercicio 20

x = input("El valor de x es: ")
y = input("El valor de y es: ")
z = input("El valor de z es: ")

print(f"El valor de x es {x}, el valor de y es {y} y el valor de z es {z}")
