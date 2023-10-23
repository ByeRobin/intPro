import random
numeros = []
i=0
while i < 10:
    nRAND = random.randrange(0,10)
    if nRAND not in numeros:
        numeros.append(nRAND)   
    elif len(numeros) >= 10:
        i = 11
    # print(numeros)


print("\nAct1")

Zoo = ["Elefante", "Jirafa","Mono"]
animal = input("Ingresa un animal: ")
Zoo.append(animal)
print(Zoo[3])

("\nAct2")
print(numeros)
def mostrarEnUnaLinea(lista):
    for i in lista:
        print(i,end=" ")
print(mostrarEnUnaLinea(numeros))


print("\nAct3")

def divisoresList(num,lista):
    for i in range(1,num+1):
        if num % i == 0:
            lista.append(i)
    print(lista)

div = []
n = int(input("Ingresa un numero entero: "))
print(divisoresList(n,div))

print("\nAct7")


def dondeAparece(lista,blanco):
    for i in range(len(lista)):
        if lista[i] == blanco:
            return i
    return -1

print(numeros,"\n ")
blanco = int(input("Ingresa un numero del 1 al 10: "))
print("\n",dondeAparece(numeros,blanco))

