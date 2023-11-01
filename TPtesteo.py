
import math
import random
# def productos():
#     with open("productos.txt") as file_object:
#         productos = file_object.read()
#         return productos


# def agregarLista(lista,algo):
#     lista = []
#     lista.append(algo)

# def lectura(lista):
#     newList = []
#     contador = 0
#     newChar = ""
#     for i in productos():
            
        
        
# listaProductos = []
# print(lectura(listaProductos))

# print(lectura())

cadena = "Arroz,1001,1037\nYerba mate,4546,4904"
contador = 0
lista = []
Char = ""
newChar = ""
nuevaLista = []
contador = 0
for i in cadena:
    if i != "," or i != '\n':
        newChar += i
    if i == '\n':
        lista.append(nuevaLista)
        nuevaLista = []
    if i == "," or i == '\n':
        contador += 1
        if contador <= 3 :
            nuevaLista.append(newChar)
            contador = 0
        newChar = Char

    print(newChar)
    print(lista)

#print(lista)
