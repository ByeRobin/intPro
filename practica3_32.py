print("/nAct30")
char = "r"
word = "programador"
newword = ""
for i in word:
    if i != char:
        newword += i
    if i == char:
        newword += "*"
print(newword)

print("\nAct32")

x = input("Ingresa tu nombre: ")
y = input("Ingresa tu apellido: ")
z = input("Ingresa solo los numeros de tu DNI: ")
legajo = ""

contador=1
for i in z:
    if contador <=3:
        legajo += i
    contador += 1
legajo+= "_"

contador = 1

for i in y:
    if contador <=3:
        legajo += i
    contador += 1

contador = 1

for i in x:
    if contador == 1 or contador == len(x) :
        legajo += i
    contador += 1 
print(legajo)

print("\nAct palindromo")
cad = "hola"
newcad = ""
for char in cad:
    newcad = char + newcad
print(newcad)


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
