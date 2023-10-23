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


print("Sistema de precios supermercado")

def dondeAparece(lista,blanco):
    for i in range(len(lista)):
        if lista[i] == blanco:
            return i
    return -1

codigo = int(input("Ingresa el codigo del producto: "))

codigos = [32,578,49]
productos = ["azucar","yerba","arroz"]
precios = ["1000$","2500","800"]

elemento = dondeAparece(codigos,codigo)
if elemento == -1:
    print("Elemento inexistente")
else: 
    print(codigo,productos[elemento],precios[elemento])
