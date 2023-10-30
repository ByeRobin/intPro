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

print("\nAct4")
def laMasCorta(lista,lista2):
    if len(lista) > len(lista2):
        return lista2
    if len(lista2) > len(lista):
        return lista
    else:
        return lista
    
print("\nAct5")

def sonFactores(n,lista):
    divisores = 0
    for i in lista:
        if n % i == 0:
            divisores += 1
    print(divisores,len(lista))
    if divisores == len(lista):
        print(divisores,len(lista))
        return True
    else:
        return False

print("\nAct6")

def elementoRepetido(lista):
    nuevaLista = []
    for i in lista:
        if i not in nuevaLista:
            nuevaLista.append(i)
    print(lista,nuevaLista)
    if nuevaLista == lista:
        return False
    else:
        return True

print("\nAct7")

def dondeAparece(lista,blanco):
    for i in range(len(lista)):
        if lista[i] == blanco:
            return i
    return -1

print(numeros,"\n ")
blanco = int(input("Ingresa un numero del 1 al 10: "))
print("\n",dondeAparece(numeros,blanco))

print("\nAct8")

def promFloat(lista):
    num = 0
    for i in lista:
        num += i
    print(num)
    return num / len(lista)

print("\nAct9")

def maximo(lista):
    max = 0
    for i in lista:
        if i > max:
            max = i
    return max
