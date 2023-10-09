import math
x = float(input("Ingresa un valor decimal: "))
print(math.sqrt(math.log(abs(1-x))))

print("\nAct mundo hola")

string = "hola mundo"
primera = ""
segunda = ""
nueva_cadena = ""

for i in string:
    primera += i
    if i == " ":
       ultima = primera

for i in string:
    segunda = segunda+i
    if i == " ":
        segunda = ""

print(segunda + " " + ultima)
